# Use the same alpine image of the previous task
FROM alpine:latest

# Install curl pkg
RUN apk add --no-cache curl

# copy config file to /app directory
COPY config.txt /app/config.txt

# Specify the default command to run when cont starts
CMD ["sh"]