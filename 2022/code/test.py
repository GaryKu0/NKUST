import json
import whois

#reply = whois.whois("sususu.dev")
reply= {'domain_name': 'sususu.dev', 'registrar': 'Google LLC', 'whois_server': 'whois.google.com', 'referral_url': None, 'updated_date': '2021-03-24T00:33:32', 'creation_date': '2021-03-19T00:33:32', 'expiration_date': '2023-03-19T00:33:32', 'name_servers': ['jerome.ns.cloudflare.com', 'lovisa.ns.cloudflare.com'], 'status': ['clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 'clientTransferProhibited https://www.icann.org/epp#clientTransferProhibited'], 'emails': ['registrar-abuse@google.com', 'dojbcbezwgdu@contactprivacy.email'], 'dnssec': 'unsigned', 'name': ['REDACTED FOR PRIVACY', 'Contact Privacy Inc. Customer 1249763893'], 'org': 'Contact Privacy Inc. Customer 1249763893', 'address': ['REDACTED FOR PRIVACY', '96 Mowat Ave'], 'city': ['REDACTED FOR PRIVACY', 'Toronto'], 'state': 'ON', 'zipcode': ['REDACTED FOR PRIVACY', 'M4K 3K1'], 'country': 'CA'}
print("-------查詢結果-----")
s="updated_date"
reply[s]=reply[s][:-15]+"年"+reply[s][5:-12]+"月"+reply[s][8:-9]+"日"
print(reply[s])