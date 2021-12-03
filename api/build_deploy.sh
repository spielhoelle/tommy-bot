docker build . -t ghcr.io/spielhoelle/telegram_bot
docker push ghcr.io/spielhoelle/telegram_bot:latest
ssh root@81.169.216.48 "docker pull ghcr.io/spielhoelle/telegram_bot"
ssh root@81.169.216.48 "docker stop telegram_bot"
ssh root@81.169.216.48 "docker rm telegram_bot"
ssh root@81.169.216.48 "docker run --name telegram_bot -p5000:5000 -d ghcr.io/spielhoelle/telegram_bot:latest"