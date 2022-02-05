# cli = {'__extra': ['  No Backup Designated Router on this network', '  No authentication']}
# print((cli['__extra'][0][0]))
# print((cli['__extra']))
#
# if isinstance(cli['__extra'][0], list):
#     cliextras = cli['__extra'][0]
#
# cli1 = {'__extra': ['  Message-digest authentication, using key id 103']}
#
# # cliextra = [cliextra for cliextra in cliextras if 'authentication' in cliextra]
# print('hi',(cli['__extra']))
# cliextra = [ extra for extra in cli1['__extra'] if 'using key id' in extra ]
# print('gg',type(cliextra[0].split()[-1]))
# assert 'No '+ 'authentication' in cliextra
#     # print(str(cliextra))
#     # print("true")

a = 19
print('hi '+ (a) + ' hy')