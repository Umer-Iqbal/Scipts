#!/bin/bash
get_file_names()
{
    ls -al | grep .csv | awk '{print $9}' > file_names.txt
}

scale_up()
{

    while read line; 
    do    
        cpu_value=`awk -F',' '{{print $2}}' $line | tail -1` # get CPU > 80
        file_name=$line
        cpu_value=`printf "%.0f\n" "$cpu_value"` # convert decimal to int
        if (( cpu_value >= 80 )) #scale up
        then 
            file_name=`echo $file_name | cut -f1 -d"-"`     #it will pick name and remove everthing after "-"
            no_of_replicas=`kubectl get rs | grep $file_name | awk '{print $3}'` #it will pick number of replicas that are running
            if (( no_of_replicas >= 1 ))
            then                
                cat file_names.txt | grep $file_name > multiple_running_pods.txt

                check=0
                var=1000   #use to pick min cpu value
                while read pods_name;
                do
                    cpu_value=`awk -F',' '{{print $2}}' $pods_name | tail -1`   #last cpu value of pod like 80 or 20
                    cpu_value=`printf "%.0f\n" "$cpu_value"` # convert decimal to int

                    if (( var > cpu_value)) #it will pick max cpu value
                    then
                        var=$cpu_value
                    fi

                    #it will check the value of cpu of all the replicas of a pods if the values of all the pods is less then 20
                    if (( var >= 80 )) #condition to scall down a value (var==cpu_value)
                    then
                        check=1
                    else
                        check=0
                    fi

                done < multiple_running_pods.txt

                if (( check == 1))
                then
                    file_name=`echo $file_name | cut -f1 -d"-"`     #it will pick name and remove everthing after "-"
                    
                    no_of_replicas=`kubectl get rs | grep $file_name | awk '{print $3}'` #it will pick number of replicas that are running
                    ((no_of_replicas+=1))
                    kubectl scale -n default deployment $file_name --replicas=$no_of_replicas
                    echo "going to scale up: "$file_name

                    sleep 40s

                fi 

            fi
        fi    
      
        
    done < file_names.txt
}

scale_down()
{

    while read line; 
    do        
        cpu_value=`awk -F',' '{{print $2}}' $line | tail -1` # get CPU > 80
        file_name=$line
        cpu_value=`printf "%.0f\n" "$cpu_value"` # convert decimal to int
        if (( cpu_value <= 50 )) #scale down
        then 
            file_name=`echo $file_name | cut -f1 -d"-"`     #it will pick name and remove everthing after "-"
            no_of_replicas=`kubectl get rs | grep $file_name | awk '{print $3}'` #it will pick number of replicas that are running
            if (( no_of_replicas >= 2 ))
            then                
                cat file_names.txt | grep $file_name > multiple_running_pods.txt   #it will store the name of replicas of pod in new file

                check=0
                var=0   # it will pick max cpu of a pod's replicas
                while read pods_name;
                do
                    cpu_value=`awk -F',' '{{print $2}}' $pods_name | tail -1`   #last cpu value of pod like 80 or 20
                    cpu_value=`printf "%.0f\n" "$cpu_value"` # convert decimal to int
                    
                    
                    if (( var < cpu_value)) #it will pick max cpu value
                    then
                        var=$cpu_value
                    fi

                    #it will check the value of cpu of all the replicas of a pods if the values of all the pods is less then 20
                    if (( var <= 50 )) #condition to scall down a value (var==cpu_value)
                    then
                        check=1
                    else
                        check=0
                    fi

                done < multiple_running_pods.txt

                if (( check == 1))
                then
                    file_name=`echo $file_name | cut -f1 -d"-"`     #it will pick name and remove everthing after "-"
                    
                    no_of_replicas=`kubectl get rs | grep $file_name | awk '{print $3}'` #it will pick number of replicas that are running
                    ((no_of_replicas-=1))
                    kubectl scale -n default deployment $file_name --replicas=$no_of_replicas
                    echo "scale downing: "$file_name

                    sleep 10s

                fi 

            fi
        fi
    done < file_names.txt

}


while true; 
do
    get_file_names

    sleep 2s

    scale_up
    scale_down
done




















#   cpu_value=`awk -F',' '{if($2>=26){print $2}}' $line | tail -1` # get CPU > 80
#         file_name=$line
#         cpu_value=`printf "%.0f\n" "$cpu_value"` # convert decimal to int
#         if (( cpu_value >= 80 )) #scale up
#         then
#             file_name=`echo $file_name | cut -f1 -d"-"`     #it will pick name and remove everthing after "-"
#             echo "going to scale up: "$file_name
#             no_of_replicas=`kubectl get rs | grep $file_name | awk '{print $3}'` #it will pick number of replicas that are running
#             ((no_of_replicas+=1))
#             kubectl scale -n default deployment $file_name --replicas=$no_of_replicas 
#             sleep 30s

#         fi