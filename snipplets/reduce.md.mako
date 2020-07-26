# Reducing AWS EBS Volumes

Assuming we want to reduce EBS, the first thing we will need to do is to make a note of the root volume’s block device name and our instance’s availability zone

1. Stop the instance
![stop_instance](images/stop_instance.png)  
2. Detach the volume from instance
![detach_volume](images/detach_volume.png)  
3. Create a new instance

5. Create an empty Amazon EBS volume with size require in the same availability zone
![volume](images/volume.png)  

6. Attach both volumes to the instance and again note all device name details.

Block Device Name Big Volume = /dev/sdb
Block Device Name Small Volume = /dev/sdg

7. Restart the Instance and Login:

Create a file system for the new volume you have created
```
sudo mkfs -t ext4 /dev/xvdg
```
Create two mount directories and mount the new volumes.
```
sudo mkdir /mnt/big
sudo mount /dev/xvdf /mnt/big
sudo mkdir /mnt/small
sudo mount /dev/xvdg /mnt/small
```
Sync big to small
```
rsync -aHAXxSP /mnt/real/ /mnt/small
```
Umount the smaller
```
umount /dev/xvdg
```
8.	Stop new instance

9.	Detach the small volume from new instance

10.	Attached the small volume to orig instance with same block device

11.	Start the orig instance

12.	Login instance #1
a.	Mount small disk
mount  /dev/xvdb /mnt/xvdb

13. After every thing is working you can remove the big volume. recommend to save it for 1-2 week before removing
