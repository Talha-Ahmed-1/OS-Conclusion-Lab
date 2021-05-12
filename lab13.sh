while(true)
do
echo "Wellcome
1: Create File
2: Create Folder
3: Change rights of file
4: Search File
5: Create Process
6: Create Thread
7: Display Processes
8: Create C/Python program file
9: Simulation of CPU schedueling algorithms
10: Quit the program
Choose an operation:"
read ask
if [ $ask == 1 ]
then 
read -p "Enter name of file: " file
touch $file
echo "File Created"
elif [ $ask == 2 ]
then 
read -p "Enter name of file: " folder
touch $folder
echo "Folder Created"
elif [ $ask == 3 ]
then 
read -p "Execute(1)/Write(2)/Read(4)/All(7): " right
read -p "Enter file name: " file
chmod $right $file
echo "Rights have been changed."
elif [ $ask == 4 ]
then 
read -p "Enter file name: " file
read -p "Enter folder/directory: " dir
found=0
for files in /home/$USER/$dir/*
do
    if [ $files == /home/$USER/$dir/$file ]
    then
        echo "File found"
        found=1
        break
    fi
done
if [ $found = 0 ]
then
echo "File not found"
fi
elif [ $ask == 5 ]
then 
echo "Create process that sorts array in asscending."
gcc -o sorting sorting.c
chmod 777 ./sorting
./sorting
elif [ $ask == 6 ]
then 
echo "Creating thread."
gcc -o thread thread.c -lpthread
chmod 777 ./thread
./thread
elif [ $ask == 7 ]
then 
echo "Displaying Processes"
ps -aux
read -p "Want to kill any process y/n" want
if [ $want == "y" ]
then
read -p "Enter process id: " pid
kill $pid
echo "Process Killed"
fi
elif [ $ask == 8 ]
then 
echo "Creating File"
read -p "Enter filename: " name
vi $file
elif [ $ask == 9 ]
then 
echo "Simulation of CPU Schedueling Algorithms"
python3 algorithms.py
elif [ $ask == 10 ]
then 
echo "Good Bye :)"
break
fi
done