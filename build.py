import base64
from pathlib import Path
from string import Template

foto = Path('Ana Helena.jpeg')
if not foto.exists():
    raise FileNotFoundError('Coloque "Ana Helena.jpeg" na mesma pasta do build.py.')

b64 = base64.b64encode(foto.read_bytes()).decode('utf-8')
img_src = f'data:image/jpeg;base64,{b64}'

google_maps_link = (
    'https://www.google.com/maps/place/R.+Carlos+Drumond+de+Andrade,+3+-+Jardim+Shangri-La,+Bauru+-+SP,+17054-635/'
    '@-22.3600471,-49.0964771,17z/data=!3m1!4b1!4m5!3m4!1s0x94bf66c2562b4337:0xb39d1793dee2b0c6!'
    '8m2!3d-22.3600471!4d-49.0939022?entry=ttu&g_ep=EgoyMDI2MDYwMi4wIKXMDSoASAFQAw%3D%3D'
)

# ─── SVG kawaii owl ───────────────────────────────────────────────────────────
# Parâmetros: sz = tamanho (viewBox 100×120), mirror = espelhar horizontalmente
def owl_svg(sz="90px", mirror=False, branch=False):
    flip = 'transform="scale(-1,1) translate(-100,0)"' if mirror else ''
    branch_el = '<ellipse cx="50" cy="115" rx="46" ry="9" fill="#a0622a" opacity=".85"/>' if branch else ''
    # pés
    feet = '''
      <g opacity=".95">
        <ellipse cx="37" cy="113" rx="8" ry="5" fill="#f5c842" transform="rotate(-12,37,113)"/>
        <ellipse cx="63" cy="113" rx="8" ry="5" fill="#f5c842" transform="rotate(12,63,113)"/>
        <line x1="32" y1="113" x2="28" y2="116" stroke="#f5c842" stroke-width="2.2" stroke-linecap="round"/>
        <line x1="37" y1="114" x2="36" y2="118" stroke="#f5c842" stroke-width="2.2" stroke-linecap="round"/>
        <line x1="42" y1="113" x2="45" y2="116" stroke="#f5c842" stroke-width="2.2" stroke-linecap="round"/>
        <line x1="58" y1="113" x2="55" y2="116" stroke="#f5c842" stroke-width="2.2" stroke-linecap="round"/>
        <line x1="63" y1="114" x2="64" y2="118" stroke="#f5c842" stroke-width="2.2" stroke-linecap="round"/>
        <line x1="68" y1="113" x2="72" y2="116" stroke="#f5c842" stroke-width="2.2" stroke-linecap="round"/>
      </g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 120"
     width="{sz}" style="display:block;filter:drop-shadow(0 4px 8px rgba(150,0,80,.22))">
  <g {flip}>
    {branch_el}
    {feet}
    <!-- corpo arredondado -->
    <ellipse cx="50" cy="88" rx="28" ry="26" fill="#fbcfe8"/>
    <!-- peito branco -->
    <ellipse cx="50" cy="93" rx="18" ry="18" fill="#fff8fc"/>
    <!-- sombra lateral suave -->
    <ellipse cx="28" cy="88" rx="8" ry="20" fill="#f9a8d4" opacity=".35"/>
    <ellipse cx="72" cy="88" rx="8" ry="20" fill="#f9a8d4" opacity=".35"/>
    <!-- asas -->
    <ellipse cx="24" cy="90" rx="10" ry="16" fill="#f9a8d4" transform="rotate(-18,24,90)"/>
    <ellipse cx="76" cy="90" rx="10" ry="16" fill="#f9a8d4" transform="rotate(18,76,90)"/>
    <ellipse cx="24" cy="90" rx="6" ry="10" fill="#fbcfe8" transform="rotate(-18,24,90)"/>
    <ellipse cx="76" cy="90" rx="6" ry="10" fill="#fbcfe8" transform="rotate(18,76,90)"/>
    <!-- corações no peito -->
    <text x="50" y="96" text-anchor="middle" font-size="6" fill="#f472b6" opacity=".8">♥ ♥</text>
    <text x="50" y="104" text-anchor="middle" font-size="5" fill="#f9a8d4" opacity=".9">♥  ♥  ♥</text>
    <!-- cabeça grande -->
    <circle cx="50" cy="58" r="30" fill="#fbcfe8"/>
    <!-- orelhas/tufos -->
    <ellipse cx="28" cy="32" rx="7" ry="11" fill="#fbcfe8" transform="rotate(-25,28,32)"/>
    <ellipse cx="72" cy="32" rx="7" ry="11" fill="#fbcfe8" transform="rotate(25,72,32)"/>
    <ellipse cx="28" cy="32" rx="4" ry="7" fill="#f9a8d4" transform="rotate(-25,28,32)"/>
    <ellipse cx="72" cy="32" rx="4" ry="7" fill="#f9a8d4" transform="rotate(25,72,32)"/>
    <!-- topete fofo -->
    <ellipse cx="50" cy="29" rx="8" ry="6" fill="#fce7f3"/>
    <ellipse cx="44" cy="27" rx="5" ry="4" fill="#fbcfe8"/>
    <ellipse cx="56" cy="27" rx="5" ry="4" fill="#fbcfe8"/>
    <!-- rosto borda suave -->
    <ellipse cx="50" cy="58" rx="22" ry="20" fill="#fff8fc" opacity=".55"/>
    <!-- olhos castanho-escuro muito grandes -->
    <circle cx="38" cy="56" r="11" fill="#3b1a0a"/>
    <circle cx="62" cy="56" r="11" fill="#3b1a0a"/>
    <!-- íris + brilho -->
    <circle cx="38" cy="56" r="8" fill="#5c2d0a"/>
    <circle cx="62" cy="56" r="8" fill="#5c2d0a"/>
    <circle cx="38" cy="56" r="5" fill="#7a3c10"/>
    <circle cx="62" cy="56" r="5" fill="#7a3c10"/>
    <!-- pupila -->
    <circle cx="38" cy="56" r="3.5" fill="#1a0a02"/>
    <circle cx="62" cy="56" r="3.5" fill="#1a0a02"/>
    <!-- brilho primário -->
    <circle cx="34" cy="51" r="2.5" fill="white" opacity=".92"/>
    <circle cx="58" cy="51" r="2.5" fill="white" opacity=".92"/>
    <!-- brilho secundário pequeno -->
    <circle cx="41" cy="59" r="1.2" fill="white" opacity=".7"/>
    <circle cx="65" cy="59" r="1.2" fill="white" opacity=".7"/>
    <!-- anel branco ao redor dos olhos -->
    <circle cx="38" cy="56" r="11" fill="none" stroke="white" stroke-width="2.5" opacity=".6"/>
    <circle cx="62" cy="56" r="11" fill="none" stroke="white" stroke-width="2.5" opacity=".6"/>
    <!-- cílios delicados -->
    <line x1="29" y1="46" x2="26" y2="43" stroke="#3b1a0a" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="32" y1="44" x2="31" y2="41" stroke="#3b1a0a" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="36" y1="44" x2="36" y2="41" stroke="#3b1a0a" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="53" y1="44" x2="53" y2="41" stroke="#3b1a0a" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="57" y1="44" x2="57" y2="41" stroke="#3b1a0a" stroke-width="1.2" stroke-linecap="round"/>
    <line x1="61" y1="44" x2="63" y2="41" stroke="#3b1a0a" stroke-width="1.2" stroke-linecap="round"/>
    <!-- bico pequeno amarelo-dourado -->
    <ellipse cx="50" cy="68" rx="5" ry="3.5" fill="#f5c842"/>
    <ellipse cx="50" cy="66" rx="5" ry="3" fill="#f5c842"/>
    <line x1="45" y1="67" x2="55" y2="67" stroke="#e0a800" stroke-width=".8"/>
    <!-- bochecha rosa suave -->
    <ellipse cx="32" cy="65" rx="6" ry="4" fill="#f9a8d4" opacity=".5"/>
    <ellipse cx="68" cy="65" rx="6" ry="4" fill="#f9a8d4" opacity=".5"/>
    <!-- laço rosa com bolinhas brancas - lado superior esquerdo -->
    <g transform="translate(18,26) rotate(-12)">
      <!-- asa esquerda do laço -->
      <ellipse cx="-7" cy="0" rx="9" ry="6" fill="#f472b6"/>
      <!-- asa direita do laço -->
      <ellipse cx="7" cy="0" rx="9" ry="6" fill="#f472b6"/>
      <!-- centro do laço -->
      <circle cx="0" cy="0" r="4" fill="#ec4899"/>
      <!-- bolinhas brancas asa esq -->
      <circle cx="-9" cy="-1" r="1.4" fill="white" opacity=".85"/>
      <circle cx="-6" cy="2" r="1.1" fill="white" opacity=".85"/>
      <circle cx="-11" cy="2" r="1" fill="white" opacity=".75"/>
      <!-- bolinhas brancas asa dir -->
      <circle cx="9" cy="-1" r="1.4" fill="white" opacity=".85"/>
      <circle cx="6" cy="2" r="1.1" fill="white" opacity=".85"/>
      <circle cx="11" cy="2" r="1" fill="white" opacity=".75"/>
      <!-- ponto brilhante centro -->
      <circle cx="0" cy="-1" r="1.5" fill="white" opacity=".7"/>
    </g>
  </g>
</svg>'''

OWL_BRANCH = owl_svg("88px", mirror=False, branch=True)   # na árvore esquerda, em cima
OWL_BL     = owl_svg("74px", mirror=False, branch=False)  # canto inf esq
OWL_BR     = owl_svg("74px", mirror=True,  branch=False)  # canto inf dir (espelhada)

HTML = Template(r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>Convite Ana Helena – 3 anos</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden}

:root{
  --pk:#ff4fa3;--pk2:#ff82c8;--pk3:#ffd6ec;
  --dk:#9b1459;--md:#e81c86;
  --gold:#ffd166;--wht:#fff;--txt:#4a1430;
}

/* ══ ENVELOPE ══ */
#envScreen{
  position:fixed;inset:0;
  background:radial-gradient(circle at 50% 30%,#ffd6ec 0%,#ff82c8 40%,#c9176e 80%,#8a0f4a 100%);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  cursor:pointer;z-index:50;
  transition:opacity .55s,transform .55s;
}
#envScreen.hide{opacity:0;transform:scale(1.06);pointer-events:none}

.env-wrap{display:flex;flex-direction:column;align-items:center;gap:clamp(10px,3vw,18px)}

.env{
  width:min(72vw,320px);aspect-ratio:1.55;
  position:relative;
  background:linear-gradient(140deg,#ffa6d8,#ffe1f0);
  border-radius:0 0 clamp(10px,3vw,18px) clamp(10px,3vw,18px);
  box-shadow:0 clamp(10px,3vw,22px) clamp(22px,6vw,50px) rgba(80,0,45,.45);
  animation:float 3s ease-in-out infinite alternate;
  overflow:visible;
}
@keyframes float{from{transform:translateY(0)}to{transform:translateY(-9px)}}
.env-flap{
  position:absolute;top:0;left:0;width:100%;height:58%;
  background:linear-gradient(140deg,#ff4fa3,#ffadd8);
  clip-path:polygon(0 0,100% 0,50% 100%);
  transform-origin:top center;
  transition:transform .55s cubic-bezier(.4,2,.5,.9);z-index:2;
}
.env.open .env-flap{transform:rotateX(180deg)}
.env:before,.env:after{content:"";position:absolute;inset:0;background:linear-gradient(140deg,transparent 49.4%,rgba(255,255,255,.28) 50%,transparent 50.6%)}
.env:after{background:linear-gradient(220deg,transparent 49.4%,rgba(255,255,255,.28) 50%,transparent 50.6%)}
.env-seal{
  position:absolute;left:50%;top:46%;transform:translate(-50%,-50%);
  width:clamp(52px,14vw,76px);height:clamp(52px,14vw,76px);
  border-radius:50%;background:var(--gold);
  display:flex;align-items:center;justify-content:center;
  font-size:clamp(26px,7vw,40px);
  box-shadow:0 4px 14px rgba(80,0,45,.28);z-index:4;
}
.tap-txt{color:#fff;font-weight:900;font-size:clamp(13px,3.5vw,17px);text-shadow:0 2px 8px rgba(0,0,0,.3)}

/* ══ INVITE ══ */
#invScreen{
  position:fixed;inset:0;
  display:none;align-items:center;justify-content:center;
  background:radial-gradient(circle at 50% 20%,#ffd6ec 0%,#ff82c8 35%,#c9176e 75%,#8a0f4a 100%);
  overflow:hidden;
}
#invScreen.show{display:flex}

.card{
  position:relative;
  width:min(98vw,420px);height:min(98dvh,860px);
  border-radius:clamp(14px,4vw,26px);overflow:hidden;
  background:linear-gradient(180deg,#ffb5d8 0%,#ffd6ec 50%,#fff8fc 100%);
  border:3px solid rgba(255,255,255,.72);
  box-shadow:0 clamp(10px,3vw,26px) clamp(28px,7vw,65px) rgba(80,0,45,.42);
  display:flex;flex-direction:column;
}

/* ── decorações ── */
.deco{position:absolute;inset:0;pointer-events:none;z-index:1}

/* tronco */
.trunk{
  position:absolute;left:-10px;top:0;bottom:0;
  width:clamp(26px,7vw,42px);
  background:linear-gradient(90deg,#6f3518,#a7602e,#7a3b1b);
  border-radius:0 18px 18px 0;
}
.branch{
  position:absolute;left:clamp(12px,5vw,26px);
  width:clamp(55px,20vw,105px);height:clamp(11px,2.8vw,20px);
  background:#8b4a22;border-radius:18px;
}
.br1{top:clamp(50px,12vh,82px);transform:rotate(-18deg)}
.br2{top:clamp(130px,28vh,190px);width:clamp(40px,14vw,70px);transform:rotate(14deg)}

/* flores */
.fl{
  position:absolute;
  width:clamp(13px,3.5vw,20px);height:clamp(13px,3.5vw,20px);
  border-radius:50%;background:#ff7fbe;
  box-shadow:7px 0 #ffbadc,-7px 0 #ffbadc,0 7px #ffbadc,0 -7px #ffbadc;
}
.fl1{left:clamp(20px,7vw,40px);top:clamp(8px,2.5vh,18px)}
.fl2{left:clamp(1px,1vw,8px);top:clamp(55px,13vh,88px);transform:scale(.72)}
.fl3{left:clamp(26px,7vw,42px);top:clamp(108px,23vh,155px);transform:scale(.65)}
.fl4{left:2px;bottom:clamp(76px,17vh,122px);transform:scale(.6)}
.fl5{left:clamp(24px,6vw,38px);bottom:clamp(28px,7vh,50px);transform:scale(.75)}

/* flores pequenas decorativas pelo fundo */
.fl-sm{
  position:absolute;
  width:clamp(8px,2vw,13px);height:clamp(8px,2vw,13px);
  border-radius:50%;background:#ff9fd6;
  box-shadow:5px 0 #ffc8e8,-5px 0 #ffc8e8,0 5px #ffc8e8,0 -5px #ffc8e8;
  opacity:.7;
}

/* corujinhas posicionadas */
.owl-pos{position:absolute;z-index:6;pointer-events:none}
/* na árvore, sentada no galho */
.owl-tree{
  left:clamp(-8px,-1vw,2px);
  top:clamp(48px,10vh,82px);
}
/* canto inferior esquerdo */
.owl-bl{
  left:clamp(2px,1vw,10px);
  bottom:clamp(28px,7vh,50px);
}
/* canto inferior direito */
.owl-br{
  right:clamp(2px,1vw,10px);
  bottom:clamp(28px,7vh,50px);
}

/* grama */
.grass{
  position:absolute;bottom:clamp(24px,5.5vh,38px);left:0;right:0;
  height:clamp(20px,4.5vh,35px);
  background:linear-gradient(180deg,transparent,#8aae5d 40%,#5b8a39);
  border-radius:50% 50% 0 0;
}
/* cerca */
.fence{
  position:absolute;bottom:0;left:0;right:0;
  height:clamp(22px,5vh,34px);
  display:flex;gap:clamp(2px,1vw,4px);justify-content:center;align-items:flex-end;padding-bottom:2px;
}
.fence i{
  display:inline-block;
  width:clamp(10px,2.4vw,16px);height:clamp(22px,5vh,32px);
  background:linear-gradient(90deg,#b9743a,#e1a768);
  border-radius:5px 5px 2px 2px;border:1px solid rgba(90,40,10,.2);
}

/* balões */
.bln{
  position:absolute;bottom:-100px;
  width:clamp(18px,4.5vw,30px);height:clamp(25px,6vw,42px);
  border-radius:50% 50% 45% 45%;
  opacity:.82;z-index:2;
  animation:blnUp linear infinite;
}
.bln:after{content:"";position:absolute;left:50%;top:100%;width:1px;height:clamp(25px,7vw,48px);background:rgba(90,0,50,.3)}
@keyframes blnUp{from{transform:translateY(0) rotate(-5deg)}to{transform:translateY(-110vh) rotate(8deg)}}

/* brilhinhos */
.sp{
  position:absolute;width:5px;height:5px;border-radius:50%;
  background:#fff;box-shadow:0 0 10px #fff,0 0 18px var(--gold);
  animation:twk 2s infinite alternate;z-index:3;
}
@keyframes twk{from{opacity:.2;transform:scale(.7)}to{opacity:1;transform:scale(1.5)}}

/* ── conteúdo ── */
.inner{
  position:relative;z-index:5;
  flex:1;overflow-y:auto;overflow-x:hidden;
  padding:clamp(8px,2vh,14px) clamp(10px,3vw,20px) clamp(6px,2vh,12px);
  scrollbar-width:none;
}
.inner::-webkit-scrollbar{display:none}

.ribbon-pill{
  display:inline-block;
  padding:clamp(4px,1vh,7px) clamp(12px,3.5vw,22px);
  border-radius:999px;
  background:linear-gradient(90deg,var(--pk),var(--pk2));
  color:#fff;font-weight:900;font-size:clamp(10px,2.4vw,13px);
  letter-spacing:.5px;text-transform:uppercase;
  box-shadow:0 4px 14px rgba(120,0,70,.28);
}
.sub{margin-top:clamp(4px,.9vh,8px);font-size:clamp(12px,3vw,16px);font-weight:900;color:#7a1749}
h1{
  font-family:Georgia,serif;font-style:italic;
  font-size:clamp(26px,8vw,50px);line-height:.92;
  color:var(--md);text-shadow:0 2px 0 #fff,0 0 16px rgba(255,255,255,.8);
}
.age-badge{
  display:inline-block;margin:clamp(3px,.7vh,6px) 0;
  padding:clamp(3px,.7vh,6px) clamp(10px,3vw,18px);
  border-radius:999px;background:#fff0f8;border:2px solid rgba(255,79,163,.4);
  font-size:clamp(12px,2.8vw,17px);font-weight:900;color:#b31262;
}
.photo{
  width:clamp(88px,24vw,136px);height:clamp(88px,24vw,136px);
  margin:clamp(4px,1vh,8px) auto;
  border-radius:50%;padding:5px;
  background:conic-gradient(var(--gold),#fff,var(--pk),var(--pk3),var(--gold));
  box-shadow:0 0 18px rgba(255,79,163,.7);
}
.photo img{width:100%;height:100%;object-fit:cover;object-position:center top;border-radius:50%}
.intro{
  margin:clamp(2px,.5vh,5px) auto clamp(4px,1vh,9px);max-width:340px;
  font-size:clamp(10px,2.6vw,13px);font-weight:700;color:#6b1741;line-height:1.3;
}
.count-hd{font-weight:900;color:#9b1459;font-size:clamp(10px,2.6vw,13px);margin-bottom:clamp(3px,.7vh,6px)}
.countdown{display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(4px,1.1vw,7px);margin-bottom:clamp(5px,1.3vh,10px)}
.cbox{
  background:rgba(255,255,255,.86);border:2px solid rgba(255,79,163,.5);
  border-radius:clamp(8px,2vw,13px);padding:clamp(5px,1.3vh,9px) 3px;
  box-shadow:0 4px 14px rgba(160,0,80,.13);
}
.cnum{font-size:clamp(15px,4.5vw,24px);font-weight:900;color:var(--md);line-height:1}
.clbl{margin-top:3px;font-size:clamp(7px,1.7vw,10px);font-weight:900;color:#7a1749}
.details{display:flex;flex-direction:column;gap:clamp(4px,.9vh,7px);margin-bottom:clamp(5px,1.3vh,10px)}
.det{
  background:rgba(255,255,255,.88);border:2px solid rgba(255,79,163,.3);
  border-radius:clamp(9px,2.2vw,15px);
  padding:clamp(5px,1.2vh,8px) clamp(8px,2.5vw,13px);
  display:flex;align-items:center;gap:clamp(6px,1.8vw,11px);text-align:left;
}
.det-icon{font-size:clamp(14px,4vw,22px);width:clamp(20px,5.5vw,30px);text-align:center}
.det b{display:block;color:#b31262;text-transform:uppercase;font-size:clamp(7px,1.8vw,10px);margin-bottom:2px}
.det span{font-size:clamp(9px,2.4vw,12px);font-weight:700;color:#4a1430;line-height:1.25}
.actions{display:flex;flex-direction:column;gap:clamp(5px,1.1vh,8px);margin-bottom:clamp(4px,.9vh,7px)}
.btn{
  display:block;text-decoration:none;border-radius:999px;
  padding:clamp(8px,2vh,12px) 16px;
  color:#fff;font-size:clamp(11px,3vw,14px);font-weight:900;
  box-shadow:0 6px 18px rgba(120,0,70,.22);text-align:center;
}
.btn-wa{background:linear-gradient(90deg,#ff2f9f,#ff82c8)}
.btn-mp{background:linear-gradient(90deg,#c21873,#ff4fa3)}
.footer{
  font-family:Georgia,serif;font-style:italic;
  font-size:clamp(17px,4.8vw,26px);color:#d9147b;
  text-shadow:0 1px 0 #fff;margin-top:clamp(2px,.5vh,5px);
}
</style>
</head>
<body>

<!-- ══ ENVELOPE ══ -->
<section id="envScreen">
  <div class="env-wrap">
    <div class="env" id="env">
      <div class="env-flap"></div>
      <div class="env-seal">🦉</div>
    </div>
    <div class="tap-txt">✉️ Toque para abrir o convite</div>
  </div>
</section>

<!-- ══ INVITE ══ -->
<section id="invScreen">
  <div class="card" id="card">

    <div class="deco" id="deco">
      <!-- tronco e galhos -->
      <div class="trunk"></div>
      <div class="branch br1"></div>
      <div class="branch br2"></div>
      <!-- flores na árvore -->
      <div class="fl fl1"></div><div class="fl fl2"></div><div class="fl fl3"></div>
      <div class="fl fl4"></div><div class="fl fl5"></div>
      <!-- flores decorativas espalhadas -->
      <div class="fl-sm" style="right:14%;top:8%"></div>
      <div class="fl-sm" style="right:8%;top:22%"></div>
      <div class="fl-sm" style="right:18%;top:38%"></div>
      <!-- grama e cerca -->
      <div class="grass"></div>
      <div class="fence" id="fence"></div>

      <!-- corujinha no galho (esquerda, topo) -->
      <div class="owl-pos owl-tree">__OWL_BRANCH__</div>
      <!-- corujinha inferior esquerda -->
      <div class="owl-pos owl-bl">__OWL_BL__</div>
      <!-- corujinha inferior direita (espelhada) -->
      <div class="owl-pos owl-br">__OWL_BR__</div>
    </div>

    <div class="inner" id="inner">
      <div style="text-align:center">
        <div class="ribbon-pill">Você está convidada! ♥</div>
        <div class="sub">Festa da</div>
        <h1>Ana Helena</h1>
        <div class="age-badge">♥ 3 anos ♥</div>

        <div class="photo">
          <img src="$IMG_SRC" alt="Foto da Ana Helena">
        </div>

        <p class="intro">Venha comemorar comigo uma tarde muito especial, colorida e cheia de carinho.</p>

        <div class="count-hd">Faltam:</div>
        <div class="countdown">
          <div class="cbox"><div class="cnum" id="dias">00</div><div class="clbl">DIAS</div></div>
          <div class="cbox"><div class="cnum" id="horas">00</div><div class="clbl">HORAS</div></div>
          <div class="cbox"><div class="cnum" id="minutos">00</div><div class="clbl">MINUTOS</div></div>
          <div class="cbox"><div class="cnum" id="segundos">00</div><div class="clbl">SEGUNDOS</div></div>
        </div>

        <div class="details">
          <div class="det">
            <div class="det-icon">📅</div>
            <div><b>Data</b><span>18 de julho de 2026</span></div>
          </div>
          <div class="det">
            <div class="det-icon">🕑</div>
            <div><b>Horário</b><span>14:00 horas</span></div>
          </div>
          <div class="det">
            <div class="det-icon">📍</div>
            <div><b>Local</b><span>Casa dos meus avós em Bauru<br>Rua Carlos Drumond de Andrade 3-170<br>Condomínio Shangrila</span></div>
          </div>
        </div>

        <div class="actions">
          <a class="btn btn-wa" id="confirmar" href="#" target="_blank" rel="noopener">💬 Confirmar presença · (11) 96426-5008</a>
          <a class="btn btn-mp" id="mapa" href="$MAPS_LINK" target="_blank" rel="noopener">📍 Como chegar – Abrir no Google Maps</a>
        </div>

        <div class="footer">Espero por você! ♥</div>
      </div>
    </div>
  </div>
</section>

<script>
(function(){
  var env=document.getElementById('env');
  var envS=document.getElementById('envScreen');
  var invS=document.getElementById('invScreen');

  function open(){
    env.classList.add('open');
    setTimeout(function(){envS.classList.add('hide');invS.classList.add('show')},540);
  }
  envS.addEventListener('click',open);
  envS.addEventListener('touchstart',open,{passive:true});

  var msg=encodeURIComponent('Olá! Confirmo presença na festa da Ana Helena.\n\nNome:\nNúmero de adultos:\nNúmero de crianças:');
  document.getElementById('confirmar').href='https://wa.me/5511964265008?text='+msg;

  var party=new Date('2026-07-18T14:00:00-03:00');
  function tick(){
    var d=Math.max(0,party-new Date());
    document.getElementById('dias').textContent=pad(Math.floor(d/864e5));
    document.getElementById('horas').textContent=pad(Math.floor(d/36e5)%24);
    document.getElementById('minutos').textContent=pad(Math.floor(d/6e4)%60);
    document.getElementById('segundos').textContent=pad(Math.floor(d/1e3)%60);
  }
  function pad(n){return String(n).padStart(2,'0')}
  tick();setInterval(tick,1000);

  var fence=document.getElementById('fence');
  for(var f=0;f<20;f++){var i=document.createElement('i');fence.appendChild(i)}

  var card=document.getElementById('card');
  for(var s=0;s<26;s++){
    var sp=document.createElement('span');sp.className='sp';
    sp.style.cssText='left:'+Math.random()*100+'%;top:'+Math.random()*100+'%;animation-delay:'+Math.random()*2+'s;position:absolute';
    card.appendChild(sp);
  }
  var cols=['#ff4fa3','#ff82c8','#ffd6ec','#ffd166','#fff'];
  for(var b=0;b<10;b++){
    var bl=document.createElement('span');bl.className='bln';
    bl.style.cssText='left:'+Math.random()*90+'%;background:'+cols[b%cols.length]+';animation-duration:'+(9+Math.random()*9)+'s;animation-delay:-'+Math.random()*10+'s';
    card.appendChild(bl);
  }
})();
</script>
</body>
</html>
""")

html = HTML.safe_substitute(IMG_SRC=img_src, MAPS_LINK=google_maps_link)

# injeta os SVGs das corujas (contêm $ que confundiriam o Template)
html = html.replace('__OWL_BRANCH__', OWL_BRANCH)
html = html.replace('__OWL_BL__',     OWL_BL)
html = html.replace('__OWL_BR__',     OWL_BR)

Path('convite.html').write_text(html, encoding='utf-8')
print('✅  Arquivo criado: convite.html')
