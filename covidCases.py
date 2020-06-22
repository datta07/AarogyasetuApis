import requests

headers={"authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTI5MTU5NDIsImlhdCI6MTU5MjgyOTU0Miwic3ViIjoiKzkxOTE4Mjc1NjU2MSIsInVzZXJuYW1lIjoiOWY0NmM3NmMtNTM5YS00YTY2LTliMTItOGU5N2I5MGZkOTJjIn0.as_Vf_Mf6qKlhY76fg2IJ2qYKv79xzJyvncCR8_AAeY",
            "pt":"9cf23ec2-d83c-4778-aca5-d7fb64ae1b2d",
            "ver":"1050"}
#note that this code will works for a while after last commit as authorization changes over a time
res=requests.get('https://webapi.swaraksha.gov.in/ncv19/stats',headers=headers)
print(res.text)
