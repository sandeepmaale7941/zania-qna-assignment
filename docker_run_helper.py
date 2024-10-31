import os
import docker
import argparse
from dotenv import load_dotenv

def create_and_run_container(image_name, container_name, env_file):
    load_dotenv(dotenv_path=env_file)

    client = docker.from_env()

    try:
        existing_container = client.containers.get(container_name)
        print(f"Container '{container_name}' already exists with ID: {existing_container.id}")
        return
    except docker.errors.NotFound:
        pass 
    try:
        container = client.containers.run(
            image=image_name,
            name=container_name,
            environment={
                "ENV": os.getenv("ENV"),
                "DATABASE_URL": os.getenv("DATABASE_URL"),
                "MY_CUSTOM_KEY": os.getenv("MY_CUSTOM_KEY"),
            },
            ports={'8000/tcp': os.getenv["PORT"]},
            detach=True,
        )
        print(f"Container '{container_name}' started with ID: {container.id}")
    except Exception as e:
        print(f"Error starting container: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Docker container with specified configuration.")
    parser.add_argument("image_name", help="The Docker image name to use.")
    parser.add_argument("container_name", help="The name to assign to the Docker container.")
    parser.add_argument("env_file", help="The path to the .env_dev file containing environment variables.")

    args = parser.parse_args()

    create_and_run_container(args.image_name, args.container_name, args.env_file)
