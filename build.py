import re,sys
src=open(sys.argv[1]).read()
import json
over=json.load(open(sys.argv[2])) if sys.argv[2]!='-' else {}
label=sys.argv[3];out=sys.argv[4]
rows=re.findall(r'\["(D[^"]+)","(2026-09-\d\d)",(\d+),"([^"]+)","(trial|feed)"',src)
assert len(rows)==24,len(rows)
T=[(2000000,800),(1000000,500),(500000,400),(100000,200),(50000,100),(10000,50),(3000,30)]
def prize(v):
    for t,p in T:
        if v>=t: return p
    return 0
import datetime
tr=[];tot=0
for i,(code,d,v,cam,w) in enumerate(rows,1):
    v=over.get(code,int(v));p=prize(v);tot+=p
    dl=datetime.date.fromisoformat(d).strftime('%-d Sep')
    url=f"https://www.instagram.com/callie.rounds/reel/{code}/"
    tr.append(f'<tr><td class="n">{i}</td><td>{dl}</td><td><a href="{url}" target="_blank" rel="noopener">{url.replace("https://www.","")}</a></td><td class="r">{v:,}</td><td class="r p{"" if p else " z"}">${p:,}</td></tr>')
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Osmomotion September 2026</title><meta name="robots" content="noindex">
<style>
:root{{--bg:#f5f6f8;--s:#fff;--ink:#17202c;--mu:#5f6c7d;--li:#dde2e9;--a:#1f5fc4;--m:#17804a;--z:#9aa5b4}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f141b;--s:#161d27;--ink:#e7ecf3;--mu:#93a1b4;--li:#263142;--a:#7aa9f0;--m:#4cc182;--z:#5f6b7b}}}}
:root[data-theme="dark"]{{--bg:#0f141b;--s:#161d27;--ink:#e7ecf3;--mu:#93a1b4;--li:#263142;--a:#7aa9f0;--m:#4cc182;--z:#5f6b7b}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif}}
.w{{max-width:860px;margin:0 auto;padding:32px 16px 48px}}
h1{{font-size:1.6rem;margin:0 0 20px}}
.t{{background:var(--s);border:1px solid var(--li);border-radius:10px;padding:16px 18px;margin-bottom:20px;display:inline-block}}
.t span{{display:block;font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--mu)}}
.t b{{font-size:2.2rem;color:var(--m);font-variant-numeric:tabular-nums}}
.box{{background:var(--s);border:1px solid var(--li);border-radius:10px;overflow-x:auto}}
table{{border-collapse:collapse;width:100%}}
th,td{{padding:9px 12px;border-bottom:1px solid var(--li);text-align:left;white-space:nowrap}}
th{{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--mu);font-weight:600}}
tr:last-child td{{border-bottom:none}}
.r{{text-align:right;font-variant-numeric:tabular-nums}}.n{{color:var(--mu)}}
.p{{font-weight:600;color:var(--m)}}.z{{color:var(--z)}}
a{{color:var(--a)}}
@media (max-width:600px){{th:nth-child(2),td:nth-child(2){{display:none}}td a{{font-size:.85rem}}th,td{{padding:8px}}}}
</style></head><body><div class="w">
<h1>#osmomotion, September 2026</h1>
<div class="t"><span>Expected income · views as of {label}</span><b>${tot:,}</b></div>
<div class="box"><table><thead><tr><th>#</th><th>Posted</th><th>Reel</th><th class="r">Views</th><th class="r">Prize</th></tr></thead><tbody>
{"".join(tr)}
<tr><td></td><td></td><td><b>Total</b></td><td></td><td class="r p">${tot:,}</td></tr>
</tbody></table></div></div></body></html>'''
open(out,"w").write(html);print(tot)
