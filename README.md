# useful-logger

To run the server webpage enter the command log.io-server
To run the file input enter the command log.io-file-input

The server webpage will look for configuration commands by default from ~/.log.io/server.json. You can change this by adding this text into your path (to change on ubuntu use nano/vim/text editor to open /etc/environment) (you can replace the directories with one of your choosing) LOGIO_SERVER_CONFIG_PATH="/home/sam/logios/server.json"

Running log.io-file-input will look for instructions from /.log.io/inputs/file.json. To change the file input configuration type this into your path (you can replace the directories with one of your choosing): 
LOGIO_FILE_INPUT_CONFIG_PATH="/home/sam/logios/inputs/file.json"

SAMPLE SERVER CONFIG FILE:
{
  "messageServer": {
    "port": 6689,
    "host": "127.0.0.1"
  },
  "httpServer": {
    "port": 6688,
    "host": "127.0.0.1"
  },
  "debug": false,
  "basicAuth": {
    "realm": "abc123xyz",
    "users": {
      "username1": "password1"
    }
  }
}

SAMPLE FILE INPUT CONFIG FILE:
{
  "messageServer": {
    "host": "127.0.0.1",
    "port": 6689
  },
  "inputs": [
    {
      "source": "server1",
      "stream": "app1",
      "config": {
        "path": "log.io-demo/file-generator/app1-server1.log"
      }
    },
    {
      "source": "server2",
      "stream": "system-logs",
      "config": {
        "path": "/var/log/**/*.log",
        "watcherOptions": {
          "ignored": "*.txt",
          "depth": 99,
        }
      }
    }
  ]
}



