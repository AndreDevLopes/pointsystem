# Documentação point system v1

## baseUrl: http//:localhost:8000/api

### Endpoints

    /login/
    /servidor/
    /servidor/horario/
    /servidor/horas/trabalhadas/
    /servidor/justificativa/
    /feriado/

### Exemplo de uso login

<b>
    Endpoint deve ser usado para fazer o login na apliacação 
    o token gerado pela api deve ser usado para autenticação nos 
    outro endpoint.
</b>

    request POST baseUrl/login/

    header:{

        "Content-Type":"application/json"
    }

    body:{
        "username": "000000-0",
        "password": "000000-0"
    }

    response status 200

    data:{
        "expiry": "2022-05-29T09:04:47.165847Z",
        "token": "bb2013ce2d9c7f8f22e350fc08268e7b5943164089ea2650b2d02ec6ad9b1b36"
    }

### Exemplo de uso servidor

<b>
    Endpoint deve retornar os dados do servidor 
</b>

    request GET baseUrl/servidor/

    header:{
        "Content-Type":"application/json",
        "Authorization":"token f69eacd59d010b8de87e6461ca418d69446598e41eeee602419dd9183ffe9f75"
    }

    response status 200

    data:[
            {
            "id": "1",
            "usuario": {
                "username": "041035-3",
                "first_name": "Andre",
                "last_name": "",
                "is_active": true,
                "is_staff": true,
                "email": "andrelopessfla@gmail.com",
                "is_superuser": true,
                "last_login": "2022-06-11T14:55:41.750866Z"
            },
            "vinculo": "CONC",
            "setor": "ADMINISTRATIVO.FUNDAMENTAL",
            "telefone": "(88) 9289-0132",
            "cargo": "Professor",
            "secretaria": {
                "id": "1",
                "nome": "SECRETARIA DE EDUCAÇÃO",
                "horarios": [
                    {
                        "dia": "SEG",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    },
                    {
                        "dia": "TER",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    },
                    {
                        "dia": "QUA",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    },
                    {
                        "dia": "QUI",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    },
                    {
                        "dia": "SEX",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    }
                ]
            }
        }
    ]

### Exemplo de uso servidor/horario

<b>
    Endpoint deve retornar o horario do servidor 
</b>

    request GET baseUrl/servidor/horario/

    header:{
        "Content-Type":"application/json",
        "Authorization":"token f69eacd59d010b8de87e6461ca418d69446598e41eeee602419dd9183ffe9f75"
    }

    response status 200

    data:[
        {
            "id": "1",
            "usuario": "041035-3",
            "secretaria": {
                "id": "1",
                "nome": "SECRETARIA DE EDUCAÇÃO",
                "horarios": [
                    {
                        "dia": "SEG",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    },
                    {
                        "dia": "TER",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    },
                    {
                        "dia": "QUA",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    },
                    {
                        "dia": "QUI",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    },
                    {
                        "dia": "SEX",
                        "entrada": "07:00:00",
                        "intervalo": "12:00:00",
                        "retorno": "13:00:00",
                        "saida": "17:00:00"
                    }
                ]
            }
        }
    ]

### Exemplo de uso servidor/horas/trabalhadas/

<b>
    Endpoint deve retornar as horas trabalhado do dia
</b>

    request GET baseUrl/servidor/horas/trabalhadas/

    header:{
        "Content-Type":"application/json",
        "Authorization":"token f69eacd59d010b8de87e6461ca418d69446598e41eeee602419dd9183ffe9f75"
    }

    response status 200

    data:[
        {
            "dia": "2022-06-04",
            "horas_trabalhadas": 32400
        }
    ]

### Exemplo de uso servidor/justificativa/

<b>
    Endpoint deve cadatrar a justificativa de falta do funcionario 
</b>

    request POST baseUrl/servidor/justificativa/

    header:{
        'Content-Type': 'multipart/form-data'
        "Authorization":"token f69eacd59d010b8de87e6461ca418d69446598e41eeee602419dd9183ffe9f75"
    }

    body:{
        tipo: "Doente",
        data_inicio:"2022-06-12",
        data_final:"2022-06-20",
        descricao:"estou doente",
        servidor:"041035-5",
        arquivo: atestado.jpg
    }

    response status 201

       {
        "id": 3,
        "tipo": "Doente",
        "data_inicio": "2022-06-12",
        "data_final": "2022-06-22",
        "descricao": "teste2",
        "servidor": "zé do teste",
        "arquivo": "http://res.cloudinary.com/dicmteqcv/image/upload/v1655516216/nt3dkflvhwjtqurxo5rm.jpg",
        "status": "PEN"
     }

### Exemplo de uso Feriado

<b> 
    O metodo GET deve retornar todos os feriado No metodo GET pode ser acresentado o query params ? data_inicial = data & data_final = data
    a api vai retorna todos os feriados nesse intervalo.
</b>

    request GET baseUrl/feriado/

    header:{
        "Content-Type":"application/json",
        "Authorization":"token f69eacd59d010b8de87e6461ca418d69446598e41eeee602419dd9183ffe9f75"
    }

    response status 200

    data:[
        {
            "dia": "2022-09-07",
            "tipo": "NAC",
            "nome": "Independência do Brasil"
        },
        {
            "dia": "2022-08-14",
            "tipo": "EST",
            "nome": "NOSSA SENHORA DA ASSUNÇÃO"
        },
        {
            "dia": "2022-12-08",
            "tipo": "MUN",
            "nome": "Feriado Municipal"
        }
    ]
