import http.client

conn = http.client.HTTPSConnection("theekshanas.auth0.com")

payload = "{\"client_id\":\"mmKxsaywn5NdL3QvjIgZe2vlLhlXzOwm\",\"client_secret\":\"SRC85cVwL3e0OaR0YQief9I1cjm6QHhjBYePR6Ua3ET1fSigJwa0t2UX12NiSPiU\",\"audience\":\"https://online-exam.sans.com.br\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))