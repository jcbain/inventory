from server import Server
from lib.init_docker import DockerClient

docker = DockerClient()
server = Server(docker)
server.start_server()