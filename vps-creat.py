import subprocess
import json

# 可用区域和大小列表
regions = [
"ams3"，
"blr1"，
"fra1"，
"lon1"，
"nyc1"，
"nyc3"，
"sfo2"，
"sfo3"，
"sgp1"，
"syd1"，
"tor1"
]

sizes = [
"s-1vcpu-1gb"
，"s-1vcpu-1gb-35gb-intel"
，"s-1vcpu-1gb-amd"
，"s-1vcpu-1gb-intel"
，"s-1vcpu-2gb"
，"s-1vcpu-2gb-70gb-intel"
，"s-1vcpu-2gb-amd"
，"s-1vcpu-2gb-intel"
，"s-1vcpu-512mb-10gb"
，"s-2vcpu-2gb"
，"s-2vcpu-2gb-90gb-intel"
，"s-2vcpu-2gb-amd"
，"s-2vcpu-2gb-intel"
，"s-2vcpu-4gb"
，"s-2vcpu-4gb-120gb-intel"
，"s-2vcpu-4gb-amd"
，"s-2vcpu-4gb-intel"
，"s-2vcpu-8gb-160gb-intel"
，"s-2vcpu-8gb-amd"
，"s-4vcpu-16gb-320gb-intel"
，"s-4vcpu-16gb-amd"
，"s-4vcpu-8gb"
，"s-4vcpu-8gb-240gb-intel"
，"s-4vcpu-8gb-amd"
，"s-4vcpu-8gb-intel"
，"s-8vcpu-16gb"
，"s-8vcpu-16gb-480gb-intel"
，"s-8vcpu-16gb-amd"
，"s-8vcpu-16gb-intel"
，"s-8vcpu-32gb-640gb-intel"
，"s-8vcpu-32gb-amd"
]

# 对区域和大小列表进行排序
regions.sort()
sizes.sort()

api_key="XXXXXXXXXXXXXXXXXXXXXXXXX"

# 用户选择区域
print("可用区域:")
for idx, region in enumerate(regions, 1):
    print(f"{idx}. {region}")
region_choice = int(input("选择区域 (输入数字): "))
region = regions[region_choice - 1]

# 用户选择大小
print("可用大小:")
for idx, size in enumerate(sizes, 1):
    print(f"{idx}. {size}")
size_choice = int(input("选择大小 (输入数字): "))
size = sizes[size_choice - 1]



# 定义 cURL 命令
# First, let's create the curl_command.txt file with the given curl command content.
curl_command = [
    "curl", "-s", "-X", "POST",
    "-H", "Content-Type: application/json",
    "-H", f"Authorization: Bearer {api_key}",
    "-d", '''
    {
        "name": "a123",
        "region": "nyc1",
        "size": "s-1vcpu-1gb",
        "image": "debian-12-x64",
        "backups": "false",
        "ipv6": "true",
        "user_data": "#!/bin/bash\\nsudo service iptables stop 2> /dev/null ; chkconfig iptables off 2> /dev/null ; sudo sed -i.bak '/^SELINUX=/cSELINUX=disabled' /etc/sysconfig/selinux; sudo sed -i.bak '/^SELINUX=/cSELINUX=disabled' /etc/selinux/config; sudo setenforce 0; echo root:Opencloud@Leige |sudo chpasswd root; sudo sed -i 's/^#\\?PermitRootLogin.*/PermitRootLogin yes/g' /etc/ssh/sshd_config; sudo sed -i 's/^#\\?PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config; sudo service sshd restart;"
    }
    ''',
    "https://api.digitalocean.com/v2/droplets"
]


curl_com=str(curl_command)

import ast

# 原始字符串
original_string = curl_com

print(region)
print(size)

original_string=original_string.replace("s-1vcpu-1gb", size)
original_string=original_string.replace("nyc1", region)

# 使用 ast.literal_eval 将字符串转换为列表
my_list = ast.literal_eval(original_string)
print(curl_command)
print(my_list)
# 执行命令
result = subprocess.run(my_list, capture_output=True, text=True)

# 输出结果
print("\n Status code:", result,"\n")
print("\n Output:", result.stdout,"\n")
print("\n Error:", result.stderr,"\n")
