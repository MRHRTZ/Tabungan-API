# Tabungan API

## Requirements
- python 3.9
- postgresql latest (or use docker instead)

## Setup
- Change `.env.example` to `.env`
- configure variable consider your own database
- if you're using docker don't change docker configuration at .env

## Running
### on Local
- `python -m pip install -r app/requirements.txt`
- `python main.py`

### or using Docker
- `docker compose up`

## Docs
This using FastAPI you can directly access the docs at [SwaggerUI](http://localhost:8000/docs)

## Examples Endpoints

> ## Daftar
### Request URL
`/api/v1/daftar`
### Payload
```json
{
  "nama": "string",
  "nik": "string",
  "no_hp": "string"
}
```
### Response
```json
{
  "trace": "672730954729346",
  "status": 200,
  "remark": "Pendaftaran berhasil",
  "result": {
    "account_no": "37380000090236"
  }
}
```
<hr /> 
<br /> 

> ## Tabung
### Request URL
`/api/v1/tabung`
### Payload
```json
{
  "no_rekening": "string",
  "nominal": 0
}
```
### Response
```json
{
  "trace": "464908369693080",
  "status": 200,
  "remark": "Saldo tabungan berhasil ditambahkan.",
  "result": {
    "saldo": 25000
  }
}
```
<hr /> 
<br /> 

> ## Tarik
### Request URL
`/api/v1/tarik`
### Payload
```json
{
  "no_rekening": "string",
  "nominal": 0
}
```
### Response
```json
{
  "trace": "275405234413099",
  "status": 200,
  "remark": "Saldo tabungan berhasil ditarik.",
  "result": {
    "saldo": 17500
  }
}
```

<hr /> 
<br /> 

> ## Mutasi
### Request URL
`/api/v1/mutasi`
### Payload
```json
{
  "nama": "string",
  "nik": "string",
  "no_hp": "string"
}
```
### Response
```json
{
  "trace": "701203017618427",
  "status": 200,
  "remark": "Berhasil mengambil data mutasi.",
  "result": {
    "mutasi": [
      {
        "waktu": "2023-06-24 06:44:37",
        "kode_transaksi": "C",
        "nominal": 25000
      },
      {
        "waktu": "2023-06-24 06:45:27",
        "kode_transaksi": "D",
        "nominal": 17500
      }
    ]
  }
}
```

## Contact Me
- [WhatsApp](https://wa.me/6285559038021)