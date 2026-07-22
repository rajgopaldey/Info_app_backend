# import os.        #os = Python module Operating System (Linux/Windows)- use -folder change command run

# def build_docker():   #def = function define /মানে Docker build করার logic এখানে রাখা হয়েছে।
#     print("Build docker") #Pipeline log-এ দেখাবে:
#     os.chdir("..") ## scripts folder theke ek step pichone root folder-e ashchhi
#     os.system("docker build -t info_app .").  #chdir = Change Directory

# if __name__ == "__main__":
#     build_docker()


import os

def build_docker():
    print("Build docker")
    
    # 1. Project root folder-e jachhi (scripts folder theke 1 step pichone)
    script_path = os.path.dirname(__file__)      # scripts folder-er path
    root_path = os.path.join(script_path, "..")  # root folder-er path
    os.chdir(root_path)                          # root folder-e change directory korlam
    
    # 2. Docker build command run korchhi
    os.system("docker build -t info_app .")
    print("✅ Docker Build Completed!")

if __name__ == "__main__":
    build_docker()
