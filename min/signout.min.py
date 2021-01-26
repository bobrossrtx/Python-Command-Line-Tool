J='logged_in'
I=open
import json as C,os
A='settings.json'
if os.path.exists(A):
	with I(A,'r')as E:
		D=C.load(E)
		for F in D['settings']:
			for G in F['preferences']:
				for B in G['user']:
					if B[J]:print('You are now logged out');B[J]=False;B['user_details']={}
				with I(A,'w')as H:C.dump(D,H,indent=2)