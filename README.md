# mslscript.com
My website, backed up. Named RoseMay.

This is a very simple web-site that works, with a little effort, on www.pythonanywhere.com. I am not so sure it 
works 100% because I am backing up in the middle of work. In the current state it uses a session cookie to access
private urls and .ini files in a users directory. Eventually the web-site will sync with a irc-only (Internet Relay Chat)
proxy server, which is no where near completion, at this time.

The web-site will be used to display stats, change proxy server settings related to IRC, provide users with a www.mslscript.com/username URL
where they may host an xdcc search engine of all xdcc channels. And **.search <*movie*>** to search any single xdcc channel, but you may use it in
multiple channels; to search multiple channels. I have not got that far in to the coding yet we'll see how it unfolds a long time from now.

The Proxy Server is on github and updated every now and again, it is Trio-Ircproxy.py. It uses the Trio mini-framework written in Python.
