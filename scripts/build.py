import os.        #os = Python module Operating System (Linux/Windows)- use -folder change command run

def build_docker():   #def = function define /মানে Docker build করার logic এখানে রাখা হয়েছে।
    print("Build docker") #Pipeline log-এ দেখাবে:
    os.chdir("..") ## scripts folder theke ek step pichone root folder-e ashchhi
    os.system("docker build -t info_app .").  #chdir = Change Directory

if __name__ == "__main__":
    build_docker()
