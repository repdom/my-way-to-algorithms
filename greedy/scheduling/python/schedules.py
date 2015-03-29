print	reduce( lambda x, y: [x[0]+y[0]*(y[1]+x[1]), x[1]+y[1]],
        	sorted(
            	[map(int, job.split(' '))
                	for job in
                    	open('jobs.txt', 'r').read().split('\n')[1:-1]],
                    	key=lambda x: [x[0]-x[1], x[0]],
                    	reverse = True),
                [0,0])[0]
