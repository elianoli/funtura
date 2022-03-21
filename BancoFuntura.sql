drop database if exists funtura;
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
    logradouro VARCHAR(100),
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
    logradouro VARCHAR(100),
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
 numParcela int,
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
	quantItem smallint unsigned default 1,
    comissaoF float default 0,
    idOS int not null,
    idFuncionario int not null,
    idServico int not null,
    idProduto int not null,
    constraint pk_itemOS primary key(idItemOS)
);

create table Servico(
	idServico int not null auto_increment,
    nomeServico varchar(50),
    valorServico float default 0,
    descServico varchar(100),
	habilitado tinyint(1),
	constraint pk_servico primary key(idServico)
);

create table Produto(
	idProduto int not null auto_increment,
    nomeProduto varchar(50),
    valorProduto float default 0,
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


###########################################################################################
###########################################################################################

#RESTRIÇÕES DE INTEGRIDADE

ALTER TABLE OrdemServico
ADD CONSTRAINT chk_valorTotal 
CHECK (valorTotal >= 0);

ALTER TABLE OrdemServico
ADD CONSTRAINT chk_numParcelas
CHECK (numParcelas >= 0);

ALTER TABLE OrdemServico
ADD CONSTRAINT chk_valorEntrada
CHECK (valorEntrada >= 0);

ALTER TABLE Parcela
ADD CONSTRAINT chk_valorParcela 
CHECK (valorParcela >= 0);

ALTER TABLE ItemOS
ADD CONSTRAINT chk_valorItemOS 
CHECK (valorItemOS >= 0);

ALTER TABLE ItemOS
ADD CONSTRAINT chk_comissaoF 
CHECK (comissaoF >= 0);

ALTER TABLE ItemOS
ADD CONSTRAINT chk_quantItem
CHECK (quantItem >= 0);

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

###########################################################################################
###########################################################################################

#VIEWS

create or replace view v_ordemservico as
select C.nomeC, OS.idOS, OS.dataHoraAbertura, OS.dataHoraFechamento, OS.estadoOS, 
		OS.valorTotal, OS.valorEntrada, OS.numParcelas, C.idCliente
from cliente C 
inner join ordemservico OS on C.idCliente = OS.idCliente
inner join parcela P on OS.idOS = P.idOS;

create or replace view v_parcelas as
select OS.idOS, P.datavencimento, P.dataPagto, P.valorParcela, P.estadoParcela 
from cliente C
inner join ordemservico OS on C.idCliente = OS.idCliente
inner join parcela P on OS.idOS = P.idOS;

create or replace view v_tabela_relatorios as
select C.nomeC, C.cpfC, V.placa, OS.dataHoraAbertura, OS.dataHoraFechamento, OS.estadoOS, OS.valorTotal, OS.valorEntrada, OS.numParcelas, 
	   P.numParcela, P.dataVencimento, P.dataPagto, P.valorParcela, P.estadoParcela
from ordemservico OS 
inner join cliente C on OS.idCliente = C.idCliente
inner join veiculo V on OS.idVeiculo = V.idVeiculo
inner join parcela P on OS.idOS = P.idOS;

create or replace view v_movimento_caixa as
select MC.idMovimento, TM.idTipoMovimento, MC.dataHoraMov, MC.valorMov, TM.tipo
from movimentocaixa MC 
inner join tipomovimento TM on  MC.idTipoMovimento = TM.idTipoMovimento;

###########################################################################################
###########################################################################################

#TRIGGERS

use funtura;
##################################################################################################
# CAIXA

#Inserir datas no futuro
drop trigger if exists t_insert_dataHoraCaixa_futuro;
delimiter //
create trigger t_insert_dataHoraCaixa_futuro
	before insert on caixa for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraAbertura, current_timestamp()) > 0 or
		datediff(new.dataHoraFechamento, current_timestamp()) > 0
    ) then 
		set mensagem = concat('Erro de trigger t_insert_dataHoraCaixa_futuro:',
        'Data inserida ainda não aconteceu: id: ', cast(new.idCaixa as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

drop trigger if exists t_update_dataHoraCaixa_futuro;
delimiter //
create trigger t_update_dataHoraCaixa_futuro
	before update on caixa for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraAbertura, current_timestamp()) > 0 or
		datediff(new.dataHoraFechamento, current_timestamp()) > 0
        ) then 
		set mensagem = concat('Erro de trigger t_update_dataHoraCaixa_futuro:',
        'Data atualizada ainda não aconteceu: id :', cast(new.idCaixa as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

#Adicionar data de abertura caso seja recebida nula
drop trigger if exists t_insert_dataHoraAberturaCaixa_nula;
delimiter //
create trigger t_insert_dataHoraAberturaCaixa_nula
	before insert on caixa for each row
begin
	if (new.dataHoraAbertura is null) then
		set new.dataHoraAbertura = current_timestamp();
	end if;
end; //
delimiter ;

#Data abertura maior que data fechamento
drop trigger if exists t_insert_dataHoraCaixa_invalida;
delimiter //
create trigger t_insert_dataHoraCaixa_invalida
	before insert on caixa for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraAbertura, new.dataHoraFechamento) > 0) then 
		set mensagem = concat('Erro de trigger t_insert_dataHoraCaixa_invalida:', 
			'Data de fechamento antes da data de abertura: ',
			cast(new.idCaixa as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

drop trigger if exists t_update_dataHoraCaixa_invalida;
delimiter //
create trigger t_update_dataHoraCaixa_invalida
	before update on caixa for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraAbertura, new.dataHoraFechamento) > 0) then 
		set mensagem = concat('Erro de trigger t_insert_dataHoraCaixa_invalida:', 
			'Data de fechamento antes da data de abertura: id: ',
			cast(new.idCaixa as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;
##################################################################################################
# CLIENTE

#Inserir datas no futuro
drop trigger if exists t_insert_dataNascC_futuro;
delimiter //
create trigger t_insert_dataNascC_futuro
	before insert on cliente for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataNascC, current_date()) > 0) then 
		set mensagem = concat('Erro de trigger t_insert_dataNascC_futuro:',
			'Data inserida ainda não aconteceu: ',
			cast(new.idCliente as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

#Inserir datas no futuro
drop trigger if exists t_update_dataNascC_futuro;
delimiter //
create trigger t_update_dataNascC_futuro
	before update on cliente for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataNascC, current_date()) > 0) then 
		set mensagem = concat('Erro de trigger t_update_dataNascC_futuro:',
			'Data inserida ainda não aconteceu: id: ',
			cast(new.idCliente as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

# Erro ao inserir um telefone incompleto
drop trigger if exists t_insert_telefoneC_tamanho;
delimiter //
create trigger t_insert_telefoneC_tamanho
	before insert on cliente for each row
begin
	declare mensagem varchar(100);
	if (length(new.telefoneC) <> 15) then 
		set mensagem = concat('Erro de trigger t_insert_telefoneC_tamanho: ',
			'Telefone incompleto: id :',
			cast(new.idCliente as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;
end; //
delimiter ;

# Erro ao atualizar para um telefone incompleto
drop trigger if exists t_update_telefoneC_tamanho;
delimiter //
create trigger t_update_telefoneC_tamanho
	before update on cliente for each row
begin
	declare mensagem varchar(100);
	if (length(new.telefoneC) <> 15) then 
		set mensagem = concat('Erro de trigger t_update_telefoneC_tamanho: ',
			'Telefone incompleto: ',
			cast(new.idCliente as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;
end; //
delimiter ;

##################################################################################################
# FUNCIONARIO

#Inserir datas no futuro
drop trigger if exists t_insert_dataNascF_futuro;
delimiter //
create trigger t_insert_dataNascF_futuro
	before insert on funcionario for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataNascF, current_date()) > 0) then 
		set mensagem = concat('Erro de trigger t_insert_dataNascF_futuro:',
			'Data inserida ainda não aconteceu: ',
			cast(new.idFuncionario as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

drop trigger if exists t_update_dataNascF_futuro;
delimiter //
create trigger t_update_dataNascF_futuro
	before update on funcionario for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataNascF, current_date()) > 0) then 
		set mensagem = concat('Erro de trigger t_update_dataNascF_futuro:',
			'Data atualizada ainda não aconteceu: ',
			cast(new.idFuncionario as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

# Erro ao inserir um telefone incompleto
drop trigger if exists t_insert_telefoneF_tamanho;
delimiter //
create trigger t_insert_telefoneF_tamanho
	before insert on funcionario for each row
begin
	declare mensagem varchar(100);
	if (length(new.telefoneF) <> 15) then 
		set mensagem = concat('Erro de trigger t_insert_telefoneF_tamanho:',
			'Telefone incompleto: id: ',
			cast(new.idFuncionario as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;
end; //
delimiter ;

# Erro ao atualizar para um telefone incompleto
drop trigger if exists t_update_telefoneF_tamanho;
delimiter //
create trigger t_update_telefoneF_tamanho
	before update on funcionario for each row
begin
	declare mensagem varchar(100);
	if (length(new.telefoneF) <> 15) then 
		set mensagem = concat('Erro de trigger t_update_telefoneF_tamanho:',
			'Telefone incompleto: ',
			cast(new.idFuncionario as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;
end; //
delimiter ;

##################################################################################################
# ITEM DE ORDEM DE SERVICO

#Comissao maior que valor do item OS
drop trigger if exists t_insert_comissaoF_superior;
delimiter //
create trigger t_insert_comissaoF_superior 
	before insert on itemos for each row
begin
	declare mensagem varchar(100);
	if(new.valorItemOS < new.comissaoF) then
		set mensagem = concat('Erro de trigger t_insert_comissaoF_superior:',
			'Valor da comissão maior do que o valor do item da ordem de serviço: id: ',
			cast(new.idItemOS as char));
		signal sqlstate '45000' set message_text = mensagem;		
    end if;
end; //
delimiter ;

drop trigger if exists t_update_comissaoF_superior;
delimiter //
create trigger t_update_comissaoF_superior 
	before update on itemos for each row
begin
	declare mensagem varchar(100);
	if(new.valorItemOS < new.comissaoF) then
		set mensagem = concat('Erro de trigger t_update_comissaoF_superior:
			Valor da comissão maior do que o valor do item da ordem de serviço: ',
			cast(new.idItemOS as char));
		signal sqlstate '45000' set message_text = mensagem;		
    end if;
end; //
delimiter ;

##################################################################################################
# MOVIMENTO DO CAIXA

drop trigger if exists t_insert_dataHoraMov_futuro;
delimiter //
create trigger t_insert_dataHoraMov_futuro
	before insert on movimentocaixa for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraMov, current_timestamp()) > 0) then 
		set mensagem = concat('Erro de trigger t_insert_dataHoraMov_futuro:',
			'Data inserida ainda não aconteceu: ',
			cast(new.idMovimento as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

drop trigger if exists t_update_dataHoraMov_futuro;
delimiter //
create trigger t_update_dataHoraMov_futuro
	before update on movimentocaixa for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraMov, current_timestamp()) > 0) then 
		set mensagem = concat('Erro de trigger t_update_dataHoraMov_futuro:',
			'Data inserida ainda não aconteceu: ',
			cast(new.idMovimento as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

#Adicionar data do movimento caso seja recebida nula
drop trigger if exists t_insert_dataHoraMov_nula;
delimiter //
create trigger t_insert_dataHoraMov_nula
	before insert on movimentocaixa for each row
begin
	if (new.dataHoraMov is null) then
		set new.dataHoraMov = current_date();
	end if;
end; //
delimiter ;

##################################################################################################
#ORDEM DE SERVICO

#Cria parcelas
drop trigger if exists t_insert_cria_parcela;
delimiter //
create trigger t_insert_cria_parcela
	after insert on ordemservico for each row
begin
    declare count int unsigned default 1;
	declare valor_parcela float;
    
    if new.numParcelas = 0 then
		insert into parcela (numParcela, dataVencimento, dataPagto, valorParcela, estadoParcela, idOS)
			values(0, current_date(), current_date(), new.valorTotal, 'QUITADA', new.idOS);
    else
		set valor_parcela = (new.valorTotal - new.valorEntrada)/new.numParcelas;
        
		if new.valorEntrada > 0 then
			insert into parcela (numParcela, dataVencimento, dataPagto, valorParcela, estadoParcela, idOS)
				values(1, current_date(), current_date(), new.valorEntrada, 'QUITADA', new.idOS);
        end if;
        
		while count <= new.numParcelas do
			insert into parcela (numParcela, dataVencimento, dataPagto, valorParcela, estadoParcela, idOS)
				values(1 + count, adddate(current_date(), interval count month), NULL, valor_parcela, 'ABERTA', new.idOS);
			set count = count + 1;
		end while;
	end if;
end; //
delimiter ;

#Inserir datas no futuro
drop trigger if exists t_insert_dataHoraOS_futuro;
delimiter //
create trigger t_insert_dataHoraOS_futuro
	before insert on ordemservico for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraAbertura, current_timestamp()) > 0 or
		datediff(new.dataHoraFechamento, current_timestamp()) > 0
    ) then 
		set mensagem = concat('Erro de trigger t_insert_dataHoraOS_futuro: ',
			'Data inserida ainda não aconteceu: ',
			cast(new.idOS as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

#Atualizar datas no futuro
drop trigger if exists t_update_dataHoraOS_futuro;
delimiter //
create trigger t_update_dataHoraOS_futuro
	before update on ordemservico for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraAbertura, current_timestamp()) > 0 or
		datediff(new.dataHoraFechamento, current_timestamp()) > 0
        ) then 
		set mensagem = concat('Erro de trigger t_update_dataHoraOS_futuro: ',
			'Data atualizada ainda não aconteceu: ',
			cast(new.idOS as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

#Data de fechamento ao FINALIZAR ou CANCELAR OS
drop trigger if exists t_update_dataHoraFechamentoOS_fechada;
delimiter //
create trigger t_update_dataHoraFechamentoOS_fechada
	before update on ordemservico for each row
begin
	if (old.estadoOS = 'ABERTA' and (new.estadoOS = 'FINALIZADA' or new.estadoOS = 'CANCELADA')) then
		set new.dataHoraFechamento = current_timestamp();
	end if;
end; //
delimiter ;

#Adicionar data de abertura caso seja recebida nula
drop trigger if exists t_insert_dataHoraAberturaOS_nula;
delimiter //
create trigger t_insert_dataHoraAberturaOS_nula
	before insert on ordemservico for each row
begin
	if (new.dataHoraAbertura is null) then
		set new.dataHoraAbertura = current_timestamp();
	end if;
end; //
delimiter ;

#Valor de entrada maior que o valor total
drop trigger if exists t_insert_dataHoraAberturaOS_nula;
delimiter // 
create trigger t_insert_dataHoraAberturaOS_nula
	before insert on ordemservico for each row
begin
	declare mensagem varchar(100);
	if (new.valorEntrada > new.valorTotal) then 
		set mensagem = concat('Erro de trigger t_insert_dataHoraAberturaOS_nula: ',
			'Valor de entrada maior que valor total: ',
			cast(new.idOS as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

#Data abertura maior que data fechamento
drop trigger if exists t_insert_dataHoraOS_invalida;
delimiter //
create trigger t_insert_dataHoraOS_invalida
	before insert on ordemservico for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraAbertura, new.dataHoraFechamento) > 0) then 
		set mensagem = concat('Erro de trigger t_insert_dataHoraOS_invalida:',
			'Data de fechamento antes da data de abertura: ',
			cast(new.idOS as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

#Data abertura maior que data fechamento
drop trigger if exists t_update_dataHoraOS_invalida;
delimiter //
create trigger t_update_dataHoraOS_invalida
	before update on ordemservico for each row
begin
	declare mensagem varchar(100);
	if (datediff(new.dataHoraAbertura, new.dataHoraFechamento) > 0) then 
		set mensagem = concat('Erro de trigger t_update_dataHoraOS_invalida: ',
			'Data de fechamento antes da data de abertura: ',
			cast(new.idOS as char));
		signal sqlstate '45000' set message_text = mensagem;
	end if;	
end; //
delimiter ;

##################################################################################################
# PARCELA

#Registrar data pagamento
drop trigger if exists t_update_dataPagtoParcela_registro;
delimiter //
create trigger t_update_dataPagtoParcela_registro
	before update on parcela for each row
begin
	if (old.estadoParcela = 'ABERTA' and new.estadoParcela = 'QUITADA') then
    
		set new.dataPagto = current_date();
        
        insert into movimentocaixa (dataHoraMov, valorMov, idOS, idCaixa, idTipoMovimento) 
        values (current_timestamp(), new.valorParcela, new.idOS, '1', '1');	

	end if;
end; //
delimiter ;

#Finaliza OS se todas parcelas quitadas
drop trigger if exists t_update_estadoParcela_todasQuitadas;
delimiter //
create trigger t_update_estadoParcela_todasQuitadas
	after update on parcela for each row
begin
	declare quant_parcelas int unsigned;
	set quant_parcelas = (select count(*) from parcela
							where idOS = new.idOS and estadoParcela = 'ABERTA'
                            group by idOS);
	if quant_parcelas = 0 then
		update ordemservico set estadoOS = 'FINALIZADA' where idOS = new.idOS;
    end if;
end; //
delimiter ;

##################################################################################################
# PRODUTO

##################################################################################################
# SERVICO

##################################################################################################
# TIPO DE MOVIMENTO DE CAIXA

##################################################################################################
# VEICULO

drop trigger if exists t_insert_placa_incompleta;
delimiter //
create trigger t_insert_placa_incompleta
	before insert on veiculo for each row
begin
	declare mensagem varchar(100);
	if (length(new.placa)  <> 7) then
		set mensagem = concat('Erro de trigger t_insert_placa_incompleta: 
			Placa contém a quantidade de números/letras diferente de 7: ',
			cast(new.idVeiculo as char));
		signal sqlstate '45000' set message_text = mensagem;		
    end if;
end; //
delimiter ;
