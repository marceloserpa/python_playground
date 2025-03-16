import subprocess

process = subprocess.Popen(['docker-compose', 'up', '-d'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output.strip())
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        for output in process.stdout.readlines():
            print(output.strip())
        break