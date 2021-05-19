make:
	gcc -o solution solution.c
	./solution
clean:
	rm solution
time:
	time ./solution