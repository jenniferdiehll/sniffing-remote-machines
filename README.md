## Sniffing remote machines

**Overview:** Project developed for academic purposes of the course of computer networks. Among many goals of the project were the execution and collection of *tcpdump* data on each peer, as well as sending the data collected by them to all peers. In addition, it was necessary to compare the chosen protocol **(SCTP)** with the others *(UDP and TCP)*. Check out the analysis below:


### 📊 Protocol analysis:
![graphic](https://user-images.githubusercontent.com/67604477/202587681-b15abd04-fcf5-44d3-ac9a-da4e79e7aff6.jpg)

### 🔌 Pre-requisites and installation:
- *Up a container:* ```docker run -it ubuntu```

- *Update/upgrade:* ```apt-get update```, ```apt-get upgrade```

- *Have git installed on it:* ```apt-get install git``` *and clone this repository* ```https://github.com/jenniferdiehll/sniffing-remote-machines.git```

- *Install dependencies:*
    - ```apt-get install python3```
    - ```apt-get install libsctp```
    - ```apt-get install python3-setuptools```
    - ```python3 setup.py install```
    - ```apt-get install python3```
    - ```apt-get install tcpdump```
- **To run:** ```python3 main.py```

### 💻 Tech and tools used on this project:
- Docker
- Tcpdump
- Wireshark
