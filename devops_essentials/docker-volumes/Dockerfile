# Use the official Alpine image
FROM ubuntu:latest

# install any dependacy necesary
RUN apt-get update && apt-get install -y \
	nano \
	&& rm -rf /var/lib/apt/lists*

# Create a volume at /data
VOLUME /data

# Command to run when the container starts
CMD ["bash']