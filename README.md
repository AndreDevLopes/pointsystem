# Documentação point system v1
## baseUrl: http//:localhost:8000/api
### Endpoints

    /login/
    /ponto/
    /ponto/update/id/
    /servidor/horario/
    /servidor/horas/trabalhadas/

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

### Exemplo de uso ponto

<b> 
    O metodo GET deve retornar o ponto do dia, o POST deve ser usado
    para registrar um ponto um, o PUT deve ser usado para atualizar o ponto
    ao longo do dia.
</b>

    request GET baseUrl/ponto/

    header:{
        "Content-Type":"application/json",
        "Authorization":"token f69eacd59d010b8de87e6461ca418d69446598e41eeee602419dd9183ffe9f75"
    }

    response status 200 

    data:[
        {
            "id": 2,
            "dia": "2022-05-28",
            "entrada": "07:00:00",
            "intervalo": "12:00:00",
            "retorno": "13:00:00",
            "saida": "17:00:00",
            "servidor": "Fulano"
        }
    ]
    



    request POST baseUrl/ponto/

    header:{
        "Content-Type":"application/json",
        "Authorization":"token f69eacd59d010b8de87e6461ca418d69446598e41eeee602419dd9183ffe9f75"
    }

    body:{
        "dia": "2022-05-28",
        "entrada": null,
        "intervalo": null,
        "retorno": null,
        "saida": null,
        "servidor":"000000-0"
    }

    response status 201 

    data:[
       {
            "id": 2,
            "dia": "2022-05-28",
            "entrada": null,
            "intervalo": null,
            "retorno": null,
            "saida": null,
            "servidor": "Fulano"
       }
    ]

    request PUT baseUrl/ponto/update/<int:id>/

    header:{
        "Content-Type":"application/json",
        "Authorization":"token f69eacd59d010b8de87e6461ca418d69446598e41eeee602419dd9183ffe9f75"
    }

    body:{
        "dia": "2022-05-28",
        "entrada": "07:00:00",
        "intervalo": null,
        "retorno": null,
        "saida": null,
        "servidor":"000000-0"
    }

    response status 201 

    data:{
	    "message": "Point updated successfully"
    }

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



