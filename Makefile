build: 
	docker build -t jcbain/clobber -f ./clobber/Dockerfile ${PWD}/clobber

clean:
	docker rmi -f jcbain/clobber

run:
	docker run -it -v /var/run/docker.sock:/var/run/docker.sock -v ${PWD}/clobber:/opt/app -v ${PWD}/:/stuffs jcbain/clobber

.PHONY: clean build run

start: .PHONY