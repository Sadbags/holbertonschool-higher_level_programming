# Use alpine image
FROM alpine:latest

VOLUME /data

# Command to run when container starts
CMD ["echo", "Hello, World!"]