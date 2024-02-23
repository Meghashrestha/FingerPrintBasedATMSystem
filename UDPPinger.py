from socket import *
from datetime import datetime
import time
serverName = '127.0.0.1'  # local machine IP: 127.0.0.1
serverPort = 12000
# create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)
# take input from user's keyboard
message=input("Client: Input lowercase sentence:")
# send it to server through the socket
clientSocket.sendto(message.encode(),(serverName, serverPort))
# wait and receive the reply from the server
clientSocket.settimeout(5.0)
rtt_array = []
min_rtt = 0
max_rtt = 0
total_rtt = 0
number_of_response = 0
num_pings = 10

for ping_seq in range(1, num_pings + 1):
    start_time = time.time()
    current_time = datetime.now()
    current_time_formatted = current_time.strftime("%H:%M:%S")
    ping_message = f"PING {ping_seq} {current_time_formatted}"

    try:
        # Sending ping to the server
        clientSocket.sendto(ping_message.encode(), (serverName, serverPort))
        # Receiving response from the server
        response, server_address = clientSocket.recvfrom(1024)
        end_time = time.time()
        if response:
            number_of_response += 1
            rtt = end_time - start_time
            rtt_array.append(rtt)
            if rtt < min_rtt:
                min_rtt = rtt
            if rtt > max_rtt:
                max_rtt = rtt
            total_rtt += rtt
            print(f"Received: {response.decode()}, RTT:{rtt} seconds")
        else:
            print(f"Assuming packet lost {ping_seq}")

    except Exception as e:
        if isinstance(e,  timeout):
            print(f"The request time is out for ping number {ping_seq}")
        else:
            print(f"An error occurred: {e}")

    time.sleep(5)

average_rtt = total_rtt / len(rtt_array)
packet_loss_rate = (1 - (number_of_response / num_pings)) * 100
print("Minimum RTT: ", min_rtt)
print("Maximum RTT: ", max_rtt)
print("Average RTT is ", average_rtt)
print(f"The packet lost rate is {packet_loss_rate}%")

# wait and receive the reply from the server
modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
# modifiedMessage is a bytes object
print("Client:", modifiedMessage.decode())
print("Client:", serverAddress)
clientSocket.close()