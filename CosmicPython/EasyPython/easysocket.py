import socket

######################################
'''
Example IPv4(www.google.com)
must be a https:// type of address
like https://www.google.com
would be put in to the function as www.google.com
'''
def IPv4(hostname):
      address = socket.getfqdn(hostname)
      IP4 = socket.gethostbyname(address)
      return IP4
#################################################
'''
Example   WebInfo(www.google.com, 'raw', 4)
1) hostname must be https:// type of website
   for example https://www.google.com would be put in to the function as www.google.com

2) data types can be: raw, stream, dgram
   put it as a string like 'raw'

3) dataset can be: 0, 1, 2, 3, 4
   for example the variable websock raw is a list containing 5 
   other variables: (family, type, proto, canonname, sockaddr) 
   in orders 0, 1, 2, 3, 4

4) subdataset is default to 0 and is only used when dataset 4 is used
   the subdataset can be either 0 or 1
'''
def WebInfo(hostname, datatype, dataset, subdataset=0):
      websockraw, websockstream, websockdgram = socket.getaddrinfo(IPv4(hostname), 80)
      #dataset = int(dataset)
      data = dict(
          raw = websockraw[dataset],#[subdataset],
          stream = websockstream[dataset],#[subdataset],
          dgram = websockdgram[dataset]#[subdataset]
          )
      return data[str(datatype)]
##############################################
