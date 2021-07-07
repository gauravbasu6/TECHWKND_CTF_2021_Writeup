Hint: You MUST return to monke to attain absolute understanding of the world (and to get the flag). See if you can become monke.

![Main Page](./ss1.png)

On logging in with Username: user and password: user, we get that only admins can be monke.

![Error](./ss2.png)

On inspecting cookie manager, we see a token cookie with the value eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidXNlciIsImlhdCI6MTYyNTU5NTU5N30.EcqW-kRAFU8yhxocC0Xvi5vPjGNsvYhcnNGcMrnTQUY
JSON Web Tokens!!!

I visited [jwt.io](https://jwt.io) and entered the token there, and it gave me a breakdown of the token.
We see that the user value in the token is set to user(the username we logged in with).
Simply changing it to admin doesn't work. We have to edit the JWT and verify it's SHA256 signature.

I downloaded [jwt_tool](https://github.com/ticarpi/jwt_tool) and used it with the famous rockyou.txt to find the key with which the JWT was signed.
Funnily enough, it was monk3.

So I went to jwt.io and edited the old token with "user" : "admin" and used the monk3 key to verify the signature to get the new token
(eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE2MjU1OTU1OTd9.uV2M_ydbcnjf7PMjcr469DXOtdSMm1Wymg9rZJ2K8oA)

Changing our cookie to this, and refreshing, we get,


![FLAG](./ss3.png)


FLAG: TECHWKND{e4t_b4n4n_thr0w_d00d00}
