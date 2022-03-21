#drop database funtura;
create database funtura;
use funtura;

create table Funcionario(
	idFuncionario int not null auto_increment,
	nomeF varchar(50) not null,
    cpfF varchar(14) unique,
    sexoF enum('Feminino','Masculino'),
    dataNascF date,
    telefoneF varchar(15),
    emailF varchar(100),
    rua VARCHAR(100),
    cidade VARCHAR(50),
    bairro VARCHAR(50),
    numCasa VARCHAR(5),
    habilitado tinyint(1),
    constraint pk_funcionario primary key(idFuncionario)
);
create table Cliente(
	idCliente int not null auto_increment,
	nomeC varchar(50) not null,
    cpfC varchar(14) unique,
    sexoC enum('Feminino','Masculino'),
    dataNascC date,
    telefoneC varchar(15),
    emailC varchar(100),
    rua VARCHAR(100),
    cidade VARCHAR(50),
    bairro VARCHAR(50),
    numCasa VARCHAR(5),
    habilitado tinyint(1),
    constraint pk_cliente primary key(idCliente)
);

create table OrdemServico(
	idOS int not null auto_increment,
    dataHoraAbertura datetime,
    dataHoraFechamento datetime,
    estadoOS enum('ABERTA','CANCELADA','FINALIZADA'),
    valorTotal float,
    valorEntrada float,
    numParcelas smallint,
    habilitado tinyint(1),
    idCliente int not null,
    idVeiculo int not null,
    constraint pk_ordemServico primary key(idOS)
);

create table Parcela(
 idParcela int not null auto_increment,
 dataVencimento date,
 dataPagto date,
 valorParcela float,
 estadoParcela enum('QUITADA','ABERTA'),
 idOS int not null,
 constraint pk_parcela primary key(idParcela)
);

create table ItemOS(
	idItemOS int not null auto_increment,
    valorItemOS float,
	quantItem smallint unsigned,
    comissaoF float,
    idOS int not null,
    idFuncionario int not null,
    idServico int not null,
    idProduto int not null,
    constraint pk_itemOS primary key(idItemOS)
);

create table Servico(
	idServico int not null auto_increment,
    nomeServico varchar(50),
    valorServico float,
    descServico varchar(100),
    habilitado tinyint(1),
	constraint pk_servico primary key(idServico)
);

create table Produto(
	idProduto int not null auto_increment,
    nomeProduto varchar(50),
    valorProduto float,
	descProduto varchar(100),
    habilitado tinyint(1),
    constraint pk_produto primary key(idProduto)
);

create table Veiculo (
    idVeiculo int not null AUTO_INCREMENT,
    placa varchar(7) unique,
    anoFab smallint,
    cor varchar(20),
    marca varchar(25),
    descVeiculo varchar(100),
    habilitado tinyint(1),
    constraint pk_veiculo primary key(idVeiculo)
);

create table MovimentoCaixa(
	idMovimento int not null auto_increment,
    dataHoraMov datetime,
    valorMov float,
    idOS int default null,
    idCaixa int not null, 
    idTipoMovimento int not null,
    constraint pk_movimentoCaixa primary key(idMovimento)
);

create table Caixa(
	idCaixa int not null auto_increment,
    dataHoraAbertura datetime,
    dataHoraFechamento datetime,
    valorCaixa float,
    constraint pk_caixa primary key(idCaixa)
);

create table TipoMovimento(
	idTipoMovimento int not null auto_increment,
    tipo enum('APORTE','SAQUE'),
    descTipoMov varchar(100),
    constraint pk_tipoMovimento primary key(idTipoMovimento)
);

### Chaves estrangeiras

ALTER TABLE OrdemServico
ADD constraint fk_ordemServico_pk_cliente foreign key(idCliente)
REFERENCES cliente(idCliente);

ALTER TABLE OrdemServico
ADD constraint fk_ordemServico_pk_veiculo foreign key(idVeiculo)
REFERENCES veiculo(idVeiculo);

ALTER TABLE Parcela
ADD constraint fk_parcela_pk_ordemServico foreign key(idOS)
REFERENCES OrdemServico(idOS);

ALTER TABLE MovimentoCaixa
ADD constraint fk_movimentoCaixa_pk_caixa foreign key(idCaixa)
REFERENCES caixa(idCaixa);

ALTER TABLE MovimentoCaixa
ADD constraint fk_movimentoCaixa_pk_tipoMovimento foreign key(idTipoMovimento)
REFERENCES TipoMovimento(idTipoMovimento);

ALTER TABLE MovimentoCaixa
ADD constraint fk_movimentoCaixa_pk_ordemServico foreign key(idOS)
REFERENCES OrdemServico(idOS);

ALTER TABLE ItemOS
ADD constraint fk_itemOS_pk_ordemServico foreign key(idOS)
REFERENCES OrdemServico(idOS);

ALTER TABLE ItemOS
ADD constraint fk_itemOS_pk_funcinario foreign key(idFuncionario)
REFERENCES funcionario(idFuncionario);

ALTER TABLE ItemOS
ADD constraint fk_itemOS_pk_servico foreign key(idServico)
REFERENCES servico(idServico);

ALTER TABLE ItemOS
ADD constraint fk_itemOS_pk_produto foreign key(idProduto)
REFERENCES produto(idProduto);

#Restrições de integridade

ALTER TABLE OrdemServico
ADD CONSTRAINT chk_valorTotal 
CHECK (valorTotal >= 0);

ALTER TABLE OrdemServico
ADD CONSTRAINT chk_numParcelas
CHECK (numParcelas >= 0);

ALTER TABLE Parcela
ADD CONSTRAINT chk_valorParcela 
CHECK (valorParcela >= 0);

ALTER TABLE ItemOS
ADD CONSTRAINT chk_valorItemOS 
CHECK (valorItemOS >= 0);

ALTER TABLE Servico
ADD CONSTRAINT chk_valorSer
CHECK (valorServico >= 0);

ALTER TABLE Produto
ADD CONSTRAINT chk_valorProduto
CHECK (valorProduto >= 0);

ALTER TABLE Veiculo
ADD CONSTRAINT chk_anoFabricacao
CHECK (anoFab >= 0);

ALTER TABLE MovimentoCaixa
ADD CONSTRAINT chk_valorMovimentado
CHECK (valorMov >= 0);


create or replace view v_ordemservico as
select C.nomeC, OS.idOS, OS.dataHoraAbertura, OS.dataHoraFechamento, OS.estadoOS, 
		OS.valorTotal, OS.valorEntrada, OS.numParcelas
from cliente C 
inner join ordemservico OS on C.idCliente = OS.idCliente
inner join parcela P on OS.idOS = P.idOS;

create or replace view v_parcelas as
select OS.idOS, P.datavencimento, P.dataPagto, P.valorParcela, P.estadoParcela 
from cliente C
inner join ordemservico OS on C.idCliente = OS.idCliente
inner join parcela P on OS.idOS = P.idOS;


#Cria parcelas
drop trigger if exists t_insert_cria_parcela;
delimiter //
create trigger t_insert_cria_parcela
	after insert
    on ordemservico
    for each row
begin
    declare count int unsigned default 1;
	declare valor_parcela float;
    
    if new.numParcelas = 0 then
		insert into parcela (dataVencimento, dataPagto, valorParcela, estadoParcela, idOS)
			values(current_date(), current_date(), valorTotal, 'QUITADA', new.idOS);
    else
		set valor_parcela = (new.valorTotal - new.valorEntrada)/new.numParcelas;
        
		if new.valorEntrada > 0 then
			insert into parcela (dataVencimento, dataPagto, valorParcela, estadoParcela, idOS)
				values(current_date(), current_date(), new.valorEntrada, 'QUITADA', new.idOS);
        end if;
        
		while count <= new.numParcelas do
			insert into parcela (dataVencimento, dataPagto, valorParcela, estadoParcela, idOS)
				values(adddate(current_date(), interval count month), NULL, valor_parcela, 'ABERTA', new.idOS);
			set count = count + 1;
		end while;
	end if;
end; //
delimiter ;

