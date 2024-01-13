import dns.resolver

resolve = dns.resolver.Resolver()
wlist = open("/usr/share/wordlists/wfuzz/general/common.txt", "r")  # choose the current path of your worldlist
subdomains = wlist.read().splitlines()

target = input("Target: ")

for subdomain in subdomains:
	try:
		sub_target = subdomain + "." + target
		result = resolve.resolve(sub_target, "A")
		for ip in result:
			print(sub_target, "->", ip)
	except:
		pass