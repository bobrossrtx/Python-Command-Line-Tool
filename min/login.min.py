k='Please try again'
j='You need to enter the correct username and uuid'
i='You are already logged in'
h=exit
b='password'
a='email'
Z='logged_in'
Y='preferences'
X=input
V='uuid'
U='settings'
N='username'
K='user'
H='r'
G=open
A=print
import json as E,os as I
A()
A('login')
A()
F='settings.json'
def c():
	with G(F,H)as B:
		C=E.load(B)
		for D in C[U]:
			for I in D[Y]:
				for J in I[K]:
					if J[Z]:A(i);h()
def W():
	if I.path.exists(F):
		with G(F,H)as D:
			C=E.load(D)
			for J in C[U]:
				for O in J[Y]:
					for B in O[K]:
						if B[Z]:A(i);h()
						else:B[Z]=True;P=[{N:L,a:M}];B['user_details']=P
					with G(F,'w')as Q:E.dump(C,Q,indent=2)
c()
C=X('Please enter your Username: ')
D=X('Please enter your UUID: ')
if I.path.exists(f"{C}_{D}.json"):
	with G(f"{C}_{D}.json",H)as J:
		O=E.load(J)
		for P in O[K]:
			for d in P[U]:
				if d[b]:Q=X('Please enter your Password: ')
if I.path.exists(F):
	with G(F,H)as J:
		O=E.load(J)
		for P in O[U]:
			for e in P[Y]:
				for f in e[K]:
					for g in f['user_settings']:
						if g[b]:
							if I.path.exists(f"{C}_{D}.json"):
								with G(f"{C}_{D}.json",H)as R:S=E.load(R)
								for B in S[K]:
									if B[N]!=C or B[V]!=D or B[b]!=Q:A();A('That json file seems to not have that data within it');A(f"Possible Problems: The file could be corrupt. The object {C}, {D} or {Q} does not exist or has the wrong value")
									else:
										L=B[N];T=B[V];M=B[a];A();A(f"You are now logged in as {L}");A();A(f"Your uuid: {T}");A(f"Your email: {M}");A()
										with G(F,H)as J:l=E.load(J)
								W()
							elif C or D or Q=='':A(j);A();A(k)
						elif I.path.exists(f"{C}_{D}.json"):
							with G(f"{C}_{D}.json",H)as R:S=E.load(R)
							for B in S[K]:
								if B[N]!=C or B[V]!=D:A();A('You json file seems to not have that data within it');A('Possible Problems: The file could be corrupt. The object username does not exist or has the wrong value')
								else:L=B[N];T=B[V];M=B[a];A();A(f"You are now logged in as {L}");A();A(f"Your uuid: {T}");A(f"Your email: {M}");A()
							W()
						elif C or D=='':A(j);A();A(k)