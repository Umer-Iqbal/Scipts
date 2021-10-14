
#read -p "Enter Minikube Container ID: " var   #it will ask container id from user from which it will get stats.csv file as writen blow line

sudo docker cp $1:/home/docker/stats.csv .     #var==$1
cat stats.csv > stats2.csv

cat stats2.csv | awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14}' > stats3.csv  #it will remove extra spaces from data

sed -i 's/k8s_server_//g' stats3.csv  #it will remove <k8s_server_> from the <stats3.csv file> from all the lines

sed -i 's/k8s_//g' stats3.csv
awk 'BEGIN{FS=OFS=" "} {sub(/_.*/,"",$2)} 1' stats3.csv > stats4.csv # it will remove everything after underscore(_)


sed -i 's/etcd/etcd-minikube/g' stats4.csv
sed -i 's/redis/redis-cart/g' stats4.csv

cat stats4.csv | awk '{print $1, $2, $3, $4, $6, $7, $8, $10, $11, $13, $14}' > stats5.csv   # it will pick only these column from stats4.csv and create new file stats5.csv with these new columns
sed -i '1 d' stats5.csv   #it will remove first line from stats5.csv
sed -i '1 i\CONTAINER_ID NAME CPU% MEM MEM_USAGE_LIMIT MEM% NET_I NET_O BLOCK_I BLOCK_O PIDS' stats5.csv #it will insert this line at the top of stats5.csv file

rm -f  stats2.csv stats3.csv stats4.csv  #it will remove these file
mv stats5.csv /home/hut/Documents/final_stats.csv            #it will rename the file stats5.csv to final_stats.csv


#awk 'BEGIN{FS=OFS=" "} {sub(/-.*/,"",$2)} 1' test.csv > test1.csv # it will remove everything after <- sign> from second column form space seprated csv file 
