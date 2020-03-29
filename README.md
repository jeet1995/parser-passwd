Goal: To parse the UNIX /etc/passwd and /etc/groups files and combine the data into a single json output.
--
Name : Abhijeet Mohanty
--

### Development environment
* **OS :** MacOS Mojave
* **IDE :** PyCharm 2019.1.2
* **Language used :** Python 3.7
* **Libraries used :** `argparse`, `json`

### Running the application
* Navigate to **parser-passwd** by executing `cd parser-passwd/`
* Add permission to execute `run.sh` by executing `chmod u + x run.sh`
* Run the bash script by executing the command `./run.sh`

### Dependencies to download

* argparse
* json

### Algorithm
* A dictionary is used to store the final results.
* Extraction from the `/etc/passwd` file : 
    * Each line is read from the file - the lines starting with `#` are filtered out.
    * Other lines are parsed based on the `:` delimiter.
    * An example :
        ```
            _uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
            _taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
            _networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
            _installassistant:*:25:25:Install Assistant:/var/empty:/usr/bin/false
        ```
    * The resultant parsed string which gives a string array helps create an entry in the dictionary.

* Extraction from the `/etc/group` file : 
    * The initial parsing a string is done as how it is for when parsing the `/etc/passwd` file.
    * Here, the group members are extracted from every line which does not start with a `#`.
    * An example : 
        ```
            wheel:*:0:root
            daemon:*:1:root
            kmem:*:2:root
            sys:*:3:root
            tty:*:4:root
        ```
    * Every group member is iterated through and is appended to a list in the dictionary.

* Finally, the contents of the dictionary were dumped as a JSON file.    

### Results
* The results are stored in the results.json
* A sample :
    ```
      {
        "nobody": {
        "uid": "-2",
        "full_name": "Unprivileged User",
        "groups": []
      },
      "root": {
        "uid": "0",
        "full_name": "System Administrator",
        "groups": [
          "certusers"
        ]
      },
      "daemon": {
        "uid": "1",
        "full_name": "System Services",
        "groups": []
      },
      "_uucp": {
        "uid": "4",
        "full_name": "Unix to Unix Copy Protocol",
        "groups": []
      },
      "_taskgated": {
        "uid": "13",
        "full_name": "Task Gate Daemon",
        "groups": []
      },
      "_networkd": {
        "uid": "24",
        "full_name": "Network Services",
        "groups": [
          "_analyticsusers"
        ]
      }
      }
    ```

