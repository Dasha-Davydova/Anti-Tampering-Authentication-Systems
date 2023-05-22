import stix2

with open('hosts.txt') as f:
    domains = f.readlines()

indicators = []
for domain in domains:
    if domain == '':
        continue
    try:
        indicator = stix2.Indicator(
            name=f'Malicious Domain: {domain}',
            pattern="[domain-name:value = '{}']".format(domain),
            pattern_type="stix",
            labels=['malicious host']
        )
        indicators.append(indicator)
    except stix2.exceptions.InvalidValueError:
        print(domain)
        continue
    

bundle = stix2.Bundle(objects=indicators)
# Write the bundle to a STIX file
with open('malicious_domains.stix', 'w') as f:
    f.write(bundle.serialize(indent=4))

