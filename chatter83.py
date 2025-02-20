DBG = False

print("Loading data...")
import w
import sdata
import kp1
import kp2
import kp3
import kp4

w = w.w
k = {}
k.update(kp1.k)
k.update(kp2.k)
k.update(kp3.k)
k.update(kp4.k)
s = sdata.s

print("Data loaded. Moving on to dictonary loading...")

d = {}
i = 0
lw = len(w)
while i < lw:
    d[w[i]] = i
    i += 1

print("Dictionary loaded.\n")

def ge(i):
    return s.get(i, {"s": 1, "a": []})

def ui(u):
    ids = set()
    for x in u.lower().split():
        if x in d:
            wid = d[x]
            
            ids.add(wid)
            for syn in ge(wid)["a"]:
                ids.add(syn)
    return ids

def fm(u):
    uid = ui(u)
    best, bestNorm = None, 0.0
    for qIDs, aIDs in k.items():
        tot, ov = 0, 0
        for i in qIDs:
            ws = ge(i)["s"]
            tot += ws
            if i in uid:
                ov += ws
        norm = ov / tot if tot else 0
        if norm > bestNorm:
            bestNorm = norm
            best = qIDs
    return best

def my_capitalize(t):
    if not t:
        return t
    return t[0].upper() + t[1:]

def rec(ans_ids):
    tokens = [w[i] for i in ans_ids]
    out = ""
    cap = True
    for t in tokens:
        if t in [".", "?", "!"]:
            out = out.rstrip() + t + " "
            cap = True
        else:
            if cap:
                t = my_capitalize(t)
                cap = False
            out += t + " "
    return out.strip()

print("Chatbot is ready! Type 'exit' to quit.")
while True:
    ip = input("You: ").strip()
    if ip.lower() == "exit":
        print("Bot: Goodbye!")
        break
    if ip.lower() == "verbose":
        DBG = True
        print("Bot: Verbosity enabled.")
        continue
    best_q = fm(ip)
    if best_q is not None:
        print("Bot:", rec(k[best_q]))
    else:
        print("Bot: I don't know the answer yet!")