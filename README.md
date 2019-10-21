<h2>Handwriting Recognition</h2>

<h3>PERSONAL THOUGHT</h3>
During the process of doing this project, I learned a lot from it and have faced lots of troubles. At the very beginning of the project, I just know the basic knowledge of Python even it is the only knowledge i familiar with in this program. In this case, I spend huge of time learning these tools and language to prepare for coding. For training and predict models, I was struggling with how to process the image into a format that the model can recognize and how to call functions across different python files. Luckily,I met a very responsible and patient tutor Dr.Zhang, he gives me many suggestions and is willing to spent a lot of leisure time helping me after class. I remember very clearly that when I was writing the Flash file, I didn't know how to call the trained model and the image processing function together. Dr.Zhang illustrated it with me clearly and comprehensively, so that I could learn deeply about the Flash while solving the problem. Additionally, when I write the flash file, even the code is correct , whenever I encapsulate the function of result judgment into a function, the function report an error and return a same result of different pictures. This problem bothered me for a long time and seriously delayed the completion of my project. After my independent thinking and careful interpretation of the code, I realize that I lack a key String to pass each picture's name into the function and insert the data into the Nosql Database. Through continuous learning efforts, my professional knowledge has been greatly improved and it also cultivated my capabilities of solving the problem and research independent, which makes me more confident to overcome difficulties. The most important thing is that after communicating with Dr.Zhang, my understanding of the computer industry has changed from programming code to a more extensive and scientific perspective, which has a very important impact on my choice of postgraduate learning direction .



<h3>INTRODCUTION & FUNCTIONS</h3>
Handwriting Recognition is a big data internship project independently completed by myself under the guidance of Dr.Zhang from MIT LIGO lab. 

User can submits a picture or image of handwriting number through curl - xpost command or upload from webpage. This program recognizes pictures uploaded by user at first, then returns the recognized number to the user. Every time a user submits a picture, all of the picture’s name, recognized result and upload time should be insert into Cassandra.

<h3>PREPARATION:</h3>

1.Make sure you have already download Docker environment and curl, you could choose this by using commands docker --version and curl --version.<br>
2.Please colon or download this project to your computer.    


<h3>MAIN STEPS</h3>

<h4>1. Run the Docker</h4>            
Type the following instructions on the command line:
<h6>$docker run --name [container name] -p 9042:9042 -d cassandr:latest</h6>


<h4>2. Run the webpage</h4>
Run the call.py, then copy and past the address into the browser.
      
      
<h4>3. Upload the picture or image </h4>      
There are 3 ways to choose and upload pictures<br>
*Choose the pictures in the Images file and then use webpage to upload<br>
*Draw and choose some number on a huge pictures (one for each time) and then use webpage to upload.
(Run picpreprocessing.py first and then run test.py. After this, you could find a picture named newimg.jpg in the Images file.)<br>
*Ues command to upload
<h6>$ curl -F "file=@[image path]" localhost:5000/upload</h6>


<h4>4. Connect to the Cassandra</h4>
This step is finished when you run the call.py because the connect.py is linked with it.


<h4>5.Check the Keyspace and Table</h4>
(You could check the data inserted into the Nosql database.)
Type the following instructions on the command line:
<h6>$docker exec -it [container name] cqlsh ----------Eg: $docker exec -it [ zyzhang-cassandra2 ] cqlsh</h6>
Then:
<h6>cqlsh> DESC KEYSPACES;  -----------find your keyspace</h6>
<h6>cqlsh> use mykeyspace;  --------------my keyspace name is mykeyspace</h6>
<h6>cqlsh:mykeyspace> select * from mytable;   --------- my table name is mytable</h6>


#########################################################################################<br>
Once you run this on terminal, the data in your Cassandra table will remember it and won't change it, even you change the original code file. Therefore, each time when you change the original code file or want to restart, you should create a new container by either add a cluster name or remove it and use the same name.
<h6>$ docker container ls  -------use to check container ID</h6>
<h6>$ docker container kill [ container ID ]</h6>
<h6>$ docker container rm [ container ID ]</h6>


