# Craigslist Deal Finder (I call him Craig)

Hi there. Welcome to my craiglsist deal finder bot. I built this bot to help me source local lumber, used tools and other goodies (car, trailer, tires etc.) in the NYC metro area. 

# Server Fucntionality
The "server" side of this bot is simply a cronjob that runs the `poll_free_nj.py` script with arguments that you define based on which item(s) you are looking for. The particulate cronjob looks like this for my current searches for  tools: 

`*/15 * * * * source ~/workspace/craig-deals/virt-craig/bin/activate && python poll_free_nj.py `
