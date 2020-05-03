#!/usr/bin/python3.6
print("content type: text/html\n\n");
print("");
import os
os.system("tput setaf 1")
print("\t\t HEY!!! welcome to docker services")
os.system("systemctl start docker")
print("\t\tDocker services are started make and launch your oun container")
os.system("tput setaf 7")
while(1):
    name = input("ENter name of your container:")
    image = int(input("select image - \n 1. centos:7 \n 2. centos:latest \n 3. ubuntu:14.7 \n 4. mysql:5.7\n 5. none of them , want to dowmload image from docker.hub\n your option:"))
    network = input("""Enter network name:""")
    print("""choose a network:\n1: Bridge \n2: Host\n3: NUll""")
    n=int(input())
    if n==1:
         net_driver = 'bridge'
    elif n == 2:
         net_driver = 'host'
    elif n == 3:
         nrt_driver = 'null'

    os.system("docker network create {0} --driver {1}".format(network,net_driver ))

    print("\n\n---Do you want to allot any centralized volume to your container for storage?   , if yes press y :")
    s = input()
    if s == 'y':
        storage = input("enter name of storage:")
        os.system("docker volume create {}".format(storage))
    

    

    if image == 1:
        os.system("tput setaf 1")
        print("PLEASE WAIT YOUR CONTAINER IS ABOUT TO LAUNCH")
        os.system("tput setaf 7")
        os.system("docker container run --network {0} -v {2}:/var/www/html --name {1} centos:7".format(network,name,storage))
        print("your container has been launched, to verify press 1: , unless press:0")
        x=int(input())
        if x==1:
            os.system("docker images")
 
    elif image == 2:
        os.system("docker container run --network {0} -v {2}:/var/www/html --name {1} centos:7".format(network,name,storage))
        print("your container has been launched, to verify press 1: , unless press:0")
        x=int(input())
        if x==1:
            os.system("docker images")

    elif image == 3:
        os.system("docker container run --network {0} -v {2}:/var/www/html --name {1} centos:7".format(network,name,storage))
        print("your container has been launched, to verify press 1: , unless press:0")
        x=int(input())
        if x==1:
            os.system("docker images")

    elif image == 4:
        print("MYSQL IMAGE NEEDS ENVIRONMANTAL VARAIBLES\n FILL UP FOLLOWING ENTRY :-\n ")
        Mysql_Root_password = input("Mysql root password:")
        Mysql_user= input("Mysql user:")
        Mysql_password = input("Mysql password:")
        Mysql_database = input("Mysql Database:")
        os.system("docker container run -dit -e MYSQL_ROOT_PASSWORD = {0} -e MYSQL_USER = {1} -e MYSQL_PASSWORD = {2} -e MYSQL_DATABASE = {3} --network {4} -v {5}:/var/www/html --name {6} centos:7".format(Mysql_Root_password,Mysql_user,Mysql_password,Mysql_database,network,storage,name))
    elif image == 5:
        print("service are not provide for those Image that needs Enviromental variables\n\n")
        image_name=input("Enter the image name:")
        image_version=input("Enter the image version:")
        print("wait..your image is about to download ")
        os.system("docker pull {}:{}".format(image_name,image_version))
        t=input()
        if t=='y':
            os.system("docker container run --network {0} -v {2}:/var/www/html --name {1} centos:7".format(network,name,storage))



        print("your container has been launched with specified image ,volume and network, to verify press 1: , unless press:0")
        x=int(input())
        if x==1:
            os.system("docker container ls")
    print("\n\n\t\t\twant to launch more container: press Y or N \n\n")
    y=input()
    if y == "Y":
        pass
    else:
      break
os.system("tput setaf 1")

while True :    
	print("""n\n------------------------------------------------------
            \t\tSERVICES INSIDE YOUR CONTAINER
            \n\n
            select option:
            1. To see all containers that you launched
            2: To inspect or to know full details about your container
            3. launch a web server inside the container
            4: ping to any site
            5: launch a wordpress infrastructure linked with mysql database
            6: To delete any container
            7: Lunch many container of same type 
            0: Exit forom here?


                """)
	os.system("tput setaf 7")
	q = int(input())
	if q ==1 :
		os.system("docker container ls")
	elif q==2:
		while True:
			print("Enter the container about which you want full details:")
			name_inspect = input()
			os.system("docker container {}".format(name_inspect))
			print("do you want to inspect more? if yes press y ,otherwise n")
			a=input()
			if a=='y':
				pass 
			else:
                		break
	elif q==3:
		name_ser = input("enter the name of container under which you want to install webserver")
		os.system("docker start {}".format(name_ser))
		#os.system("docker attach {}".format(name_ser))
		os.system("docker exec {} yum install httpd".format(name_ser))
		os.system("docker attach {}".format(name_ser))

	elif q==4:
		print("Make sure your internet connectivity is proper")
		site = input("enter full name of site")
		os.system("curl {}".format(site))
	elif q==5:
		print("Please Wait While We are installing Dependencies")
		os.system("docker pull wordpress:5.1.1-php7.3-apache")
		os.system("docker pull mysql:5.7")
		os.system("mkdir Wordpress_Infrastructure")
		os.system("git init")
		os.system("git clone https://github.com/nandinish/Wordpress-Infrastructure")
		os.chdir("Wordpress-Infrastructure")
		os.system("docker-compose up")
	elif q==6:
		while True:
			os.system("docker ps -a")
			os.system("Give the name of container that you want to delete:")
			delete=input()
			os.system("docker rm -f {}".format(delete))
			print("Do you want to delete another container, if yes press y otnerwise n ?")
			x=input()
			if x=='y':
				pass
			else :
				break
	elif q==7:
		print("Enter the container name of which similar many containers you want to launch ")
		cont_as_img = input()
		n= input("Enter the number of containers that you want to launch")
		name_general = input("give a general name of all your container")
		i=1
		while i<n:
			os.system("docker commit {}i {}".format(name_general,cont_as_img))
			print("container ", i ,"has launched")
			i=i+1
     
	elif q==0:
		exit()
     
	print("do you like to countinue?, if yes then press y")
	ch = input()
	if ch == 'y':
		pass
	else :
		break
