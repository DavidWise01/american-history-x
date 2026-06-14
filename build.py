#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build AMERICAN HISTORY X (AHX) — Tony Kaye's 1998 anti-hate drama, catalogued into UD0 as the ELEVENTH
film-world. Themed to its MEDIUM: the film shoots the hateful past in BLACK-AND-WHITE and the present in
COLOR, so the page is monochrome with restrained colour as the present/redemption. Grave throughout; no
decorative hate iconography. Standing template, with the deep-dive = THE DEBATE (the real, documented
critique: does the film glamorize what it condemns?), sided firmly anti-hate. CARBONS (the cast, each
+.shadow real-life User — TRON) and SYNTHS (the two timelines, the reckoning, the cycle). Self-contained.
Cast & facts web-verified: the shooter is LITTLE HENRY (not Lawrence); two victims (one shot, one
curb-stomped); voluntary manslaughter, 3 yrs; reform = Lamont's friendship + the Aryan Brotherhood's
betrayal; New Line 1998; Norton Best-Actor nom; Kaye disowned it (wanted 'Humpty Dumpty', DGA refused
'Alan Smithee', sued ~$200M, lost — name stayed). The 'too-seductive' critique is real and scholarly."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "AHX"
REC = {
 "name": "AMERICAN HISTORY X", "axiom": AX,
 "position": "American History X · New Line Cinema · 1998 — dir. Tony Kaye",
 "origin": "Venice Beach, California — a family, a dead father, and the charismatic movement that fills the vacuum",
 "mechanism": "Crystallized from the film — a two-timeline anti-hate drama: a reformed neo-Nazi, just out of prison, races to pull his younger brother off the same path before the hatred they shared takes him too.",
 "crystallization": "Because it is a film whose form is its thesis — the hateful past in black-and-white, the present in colour — and whose hardest truth is that reform can come too late to save the person you love.",
 "nature": "American History X — the cautionary drama: how hate is taught at the dinner table, how it can be unlearned through human contact, and how its cost can outrun the change.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (1998, dir. Tony Kaye; New Line Cinema); the real, documented critical debate about whether it glamorizes what it condemns",
 "witness": "A young man who murdered out of hate comes home reformed, through a Black man's offered friendship and a Black teacher's refusal to give up on him — and finds the cost of the hatred he spread waiting for his brother.",
 "role": "the eleventh film-world of UD0",
 "seal": "The past in black and white, the present in colour. Hate is taught and can be unlearned — but the cost can outrun the change. Side with the ones who pull you out.",
 "source": "American History X (1998), catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#cfcdc6", "flesh-and-blood — the family the hatred moves through: Danny, the mother, the sister, the boyfriend at the dinner table; the people it costs"),
 "ethereal":  ("#5f8a9b", "the turn & the colour — Derek's reform, Lamont's offered friendship, Dr. Sweeney's patience; the present the film shoots in colour because it can still change"),
 "electrical":("#9aa0a6", "the machinery of hate — Cameron the propagandist, the movement, the foot-soldiers, the dinner-table transmission; the apparatus that manufactures it"),
 "spiritual": ("#8c3b3b", "the wound & the cost — the crime, the father's seed, the cycle, the boy who fires the last shot; the grief the film refuses to resolve"),
}

ARC_OVERALL = ("Derek Vinyard, a charismatic young neo-Nazi in Venice Beach, murders two Black men attempting to steal "
  "and vandalize his truck — shooting one and curb-stomping the other — and serves three years for voluntary manslaughter. "
  "In prison he is slowly reformed: through a working friendship with a Black inmate, Lamont, and through disillusion with, "
  "and a brutal betrayal by, the Aryan Brotherhood. He comes home renouncing the movement, determined to pull his adoring "
  "younger brother Danny off the same path — while Danny writes a school paper about him, assigned by their teacher Dr. "
  "Sweeney and titled 'American History X.' The film is told across two timelines: the hateful past in black-and-white, the "
  "present in colour.")
ARC = [
 ("I · the past, in black and white", "how the hate was taught",
  "In monochrome flashback: a father's casual racism at the dinner table, a dead father's vacuum, and the charismatic movement-leader Cameron who fills it. Derek becomes the movement's brightest, most articulate weapon — and commits the killing that sends him to prison. The black-and-white is the worldview: no middle ground."),
 ("II · the prison turn", "Lamont, and the betrayal",
  "Inside, Derek's certainty cracks. A forced laundry-detail friendship with Lamont, a Black inmate, undoes the abstraction of his hate; watching the Aryan Brotherhood deal and lie undoes his faith in the cause; and a savage assault by that same Brotherhood finishes it. He leaves prison a different man — and the film moves into colour."),
 ("III · the present, in colour", "too late for Danny",
  "Out, Derek tries to pull Danny back from Cameron and the movement, with Dr. Sweeney's help. For one night it seems to work. But the next morning Danny is shot and killed at school by Little Henry, a boy he had antagonized — the hatred recoiling faster than the reform. The film refuses catharsis: change came, and came too late."),
]

# THE DEBATE — the deep-dive (does the film glamorize what it condemns? — sided anti-hate)
DEBATE = [
 ("Black-and-white, and colour", "the form is the thesis",
  "The single most important formal choice: the past — Derek inside the movement — is shot in black-and-white, and the present, after he leaves it, in colour. The reading is plain and powerful: hate is a black-and-white worldview, all certainty and no middle ground, and the colour is the messy human world you re-enter only when you put the certainty down. The medium is the message."),
 ("The seductive-Derek problem", "the central, documented critique",
  "The honest difficulty, named openly: Norton's Derek is charismatic, articulate, physically commanding, and his white-power arguments are rarely directly rebutted on screen. Critics have argued the film risks 'fascist aesthetics' (Riefenstahl comparisons), and it retains a real neo-Nazi fan following despite its intent. The film's power and its danger are the same thing — it makes the hate vivid in order to dismantle it, and not every viewer follows it to the dismantling."),
 ("The counterweight: Lamont & Sweeney", "change comes through contact, not argument",
  "The film's answer to the hate is not a better debate — it's a relationship. Derek is pulled out by Lamont's offered friendship in the laundry and by Dr. Sweeney's patient refusal to give up on either brother. The hopeful core of the film is that hatred, learned through proximity to the wrong people, is unlearned through proximity to the right ones. Side with them, not with Derek's monologues."),
 ("The ending denies catharsis", "the cost outruns the change",
  "Derek reforms — and it does not save Danny, who is shot the next morning by Little Henry, a boy he had antagonized. The film deliberately refuses the redemption bow: it will not let the reform feel like a reward. Hate, once spread, recoils, and the recoil is faster than the change. That refusal is the film's gravest and most honest move."),
 ("The film at war with itself", "Kaye vs. New Line & Norton",
  "Off-screen, a fitting irony: director Tony Kaye fought New Line and Edward Norton over the final cut (Norton was involved in re-editing). Kaye tried to disown it — he wanted the credit changed to 'Humpty Dumpty,' the DGA refused him the 'Alan Smithee' pseudonym, and he sued for a reported ~$200M and lost. His name stayed on the film. A movie about a man at war with his own past, made by a director at war with his own movie."),
]
REALFLUFF = [
 ("The black-and-white past / colour present is deliberate", "DELIBERATE", "the form IS the meaning — the rigid 'black-and-white' certainty of hate versus the colour of the human world after it"),
 ("The film risks glamorizing what it condemns", "DEBATED", "a real, scholarly critique — Derek is charismatic and rarely rebutted on screen, and the film has a real neo-Nazi fan following despite its anti-hate intent; the honest reading sides against the hate"),
 ("Derek's reform is earned", "EARNED", "two-pronged: a cross-racial friendship with Lamont in the prison laundry, and disillusion with — then brutal betrayal by — the Aryan Brotherhood"),
 ("The ending lets Derek save his brother", "FALSE · TRAGIC", "it refuses catharsis — Danny is shot and killed at school the next morning by Little Henry, a boy he'd antagonized; hate recoils faster than reform"),
 ("The curb-stomp is among the most disturbing scenes in film", "INFAMOUS", "a racially-motivated murder depicted with deliberate horror — the two Black men are victims of a hate crime, full stop, not scene-setting"),
 ("Edward Norton was Oscar-nominated", "REAL", "Best Actor, 71st Academy Awards (lost to Roberto Benigni for Life Is Beautiful)"),
 ("Director Tony Kaye disowned the film", "CONTESTED", "he fought New Line & Norton over the cut, sought to remove his name ('Humpty Dumpty'; the DGA refused 'Alan Smithee'), sued ~$200M — and lost; his name stayed on"),
 ("The film is unambiguously anti-hate", "TRUE", "its subject is the cost of hate and the possibility — and the limits — of leaving it behind"),
]
REALFLUFF_VERDICT = ("Bottom line: American History X is a sincere anti-hate drama whose power and whose problem are the same — it "
  "makes the hatred vivid and charismatic in order to dismantle it, and not every viewer follows it all the way to the "
  "dismantling, which is why the 'too-seductive' critique is real and worth stating plainly. The right way to watch it is to "
  "hold both at once: the craft is real, the warning is real, and the seduction is exactly the thing it's warning you about. "
  "Side with Lamont and Dr. Sweeney — the people who pulled Derek out — not with the version of Derek that needed pulling; "
  "keep the two murdered men in view as victims of a hate crime; and don't look away from the ending, which refuses to let "
  "reform feel like a reward. The black-and-white was never neutral. It was the worldview the whole film is trying to leave.")

MESSAGE = ("American History X is a film about how hate is taught — at the dinner table, by a charismatic mentor, in the vacuum "
  "a dead father leaves — and how hard, and how incomplete, the unlearning is. Its form is its argument: the past is shot in "
  "black-and-white, the rigid, no-middle-ground world of the movement, and the present in colour, the messy human world Derek "
  "re-enters when he finally puts the certainty down. The reform is real and it is earned — through a Black man's offered "
  "friendship and a Black teacher's refusal to give up on him — but the film's last, unbearable move is to deny that reform its "
  "reward: Danny dies anyway, the morning after, shot by a boy the brothers' hatred helped create. The cost outran the change. "
  "The honest thing to say is that the movie's danger and its power are one: it makes the hate charismatic to show you how it "
  "works, and the work of watching it is to refuse the seduction — to stand with the people who pulled Derek out, not with the "
  "version of him that needed pulling. Hate is taught; it can be unlearned; and sometimes the unlearning comes too late to save "
  "the person you love. That is not a reason for despair. It is the reason to start sooner.")
MESSAGE_SEAL = "The past in black and white, the present in colour. Hate is taught and can be unlearned — but the cost can outrun the change. Side with the ones who pull you out, and start sooner."

SECTIONS = [
 ("The Production", "the ensemble and the studio", [
   ("Tony Kaye", "director", "a celebrated commercials/photography director making his feature debut — who would spend years at war with the film over its final cut (see The Authorship War)"),
   ("New Line Cinema · 1998", "studio & release", "a modestly-budgeted drama that became a defining anti-hate film of its decade, widely taught and debated since"),
   ("Edward Norton", "Derek Vinyard — Best Actor nominee", "nominated for the Academy Award for Best Actor (71st Academy Awards), in one of the most discussed performances of the '90s — its force is also the heart of the film's central debate"),
   ("the ensemble", "the family and the movement", "Edward Furlong (Danny), Beverly D'Angelo (mother Doris), Avery Brooks (Dr. Sweeney), Stacy Keach (Cameron), Elliott Gould (Murray), Fairuza Balk (Stacey), Guy Torry (Lamont), Ethan Suplee (Seth)"),
 ]),
 ("The Authorship War", "a film at war with its own director", [
   ("the cut", "Kaye vs. Norton & New Line", "Kaye clashed with the studio and with Edward Norton, who was involved in re-editing the film into the released version Kaye rejected"),
   ("'Humpty Dumpty'", "the disowning", "Kaye tried to remove his name, asking to be credited as 'Humpty Dumpty'; the DGA refused him the standard 'Alan Smithee' pseudonym because he had publicly disparaged the film"),
   ("the lawsuit", "~$200M, and a loss", "Kaye sued the DGA and New Line for a reported ~$200 million and lost; his name remained on the finished film"),
   ("the irony", "the war mirrors the subject", "a film about a man at war with his own past became a film at war with its own authorship — present this as contested studio history (Kaye's account is one-sided); the verifiable fact is that his name stayed"),
 ]),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — the cast, each +.shadow real-life User ──
 E("derek-vinyard","Derek Vinyard","carbon","ethereal","the reformed one",
   "Derek Vinyard — the charismatic neo-Nazi who murders out of hate, and comes out of prison renouncing the movement he was the brightest weapon of.",
   "The turn the film is built on: the most persuasive voice for hate becoming the most determined to undo it — and the heart of the debate about whether the film makes him too compelling.",
   "From the black-and-white past to the colour present; from the movement to the laundry to his brother's side.",
   "Because the film needs to show that the unlearning is possible — and to be honest that the charisma that made him dangerous never fully leaves the frame.",
   "By having his certainty broken in prison, by Lamont's friendship and the Brotherhood's betrayal, and by racing home to save Danny.",
   "I was the best thing the movement had. The work of the rest of my life is to be the worst thing that ever happened to it.",
   actor="Edward Norton", analog="the reformed extremist — the charisma that has to be refused even as it's understood"),
 E("danny-vinyard","Danny Vinyard","carbon","natural","the brother being shaped",
   "Danny Vinyard — Derek's adoring younger brother, drifting into the same movement, assigned to write a paper about Derek titled 'American History X.'",
   "The stakes made human: the boy whose path is still open, whom the whole film is a race to save — and doesn't.",
   "At school, at home, in the orbit of the brother he worships.",
   "Because the film's question is whether the cycle can be broken in time, and Danny is the test.",
   "By idolizing Derek, absorbing the hate, writing the paper that reckons with it — and dying the next morning anyway.",
   "I wrote it all down — what my brother was, and what he became. I finished the paper. I didn't get to finish anything else.",
   actor="Edward Furlong", analog="the next link in the chain — the one the reform was racing to reach"),
 E("dr-sweeney","Dr. Bob Sweeney","carbon","ethereal","the teacher who won't give up",
   "Dr. Bob Sweeney — the brothers' Black history teacher, who assigns the 'American History X' paper and refuses to abandon either of them.",
   "The film's patience: the man who answers hatred not with an argument but with persistent, unearned care.",
   "In the classroom, at the prison, at the family's door — always reaching.",
   "Because the film's hope has a face, and it is a Black educator choosing, again and again, not to give up.",
   "By mentoring Danny, visiting Derek, and modelling the contact that does what no debate can.",
   "I asked you one question once: has anything you've done made your life better? Keep asking it. I'm not giving up on you.",
   actor="Avery Brooks", analog="the patient mentor — care as the answer to hate"),
 E("cameron-alexander","Cameron Alexander","carbon","electrical","the propagandist",
   "Cameron Alexander — the older white-power movement leader who grooms charismatic young men like Derek and Danny into weapons.",
   "The machinery of recruitment: the adult who manufactures hatred in the vulnerable and keeps his own hands clean.",
   "Behind the scenes of the movement, dealing influence and ideology.",
   "Because the film insists the hate is taught — and Cameron is the teacher of it, the dark mirror of Sweeney.",
   "By spotting grief and vacancy in boys and filling it with a cause, an enemy, and a use for their anger.",
   "I don't get my hands dirty. I find the angry boys, and I give their anger a shape. The movement runs on what I make of them.",
   actor="Stacy Keach", analog="the recruiter of hate — the dark mirror of the teacher"),
 E("doris-vinyard","Doris Vinyard","carbon","natural","the mother who watches it take her sons",
   "Doris Vinyard — the ailing mother who watches the movement consume one son and reach for the other, powerless against it.",
   "The family's grief in real time: a parent forced to see what was planted at her own table grow into something that kills.",
   "At home, sick and afraid, between her sons and the thing pulling them away.",
   "Because the cost of the hatred is domestic, and she is the one who pays it in fear.",
   "By failing to stop what a dead husband's prejudice began, and loving her sons through the ruin of it.",
   "I buried their father and watched his worst lesson outlive him in my boys. A mother can love and still be powerless.",
   actor="Beverly D'Angelo", analog="the grieving mother — the household cost of inherited hate"),
 E("stacey","Stacey","carbon","electrical","the movement's grip",
   "Stacey — Derek's girlfriend, fully embedded in the movement and bitter at his defection from it.",
   "The pull backward: the relationship that ties Derek to the life he's trying to leave, and resents the leaving.",
   "Inside the movement, at the party, against Derek's change.",
   "Because leaving a hate movement means leaving people, and the film shows the cost of that too.",
   "By staying true to the cause as Derek abandons it, and treating his reform as betrayal.",
   "You don't get to just walk out. We were a family in here. Leaving us is the only thing I'll never forgive.",
   actor="Fairuza Balk", analog="the partner left inside — the human cost of leaving the movement"),
 E("seth","Seth Ryan","carbon","electrical","the foot-soldier",
   "Seth Ryan — the heavyset, crude movement member who mentors Danny in Derek's absence.",
   "The movement at its ugliest and least glamorous: the bigotry stripped of Derek's articulacy, just rage and slurs.",
   "Around the Vinyard house and the movement's lower ranks.",
   "Because the film shows hate at every register — and Seth is its dumbest, plainest face.",
   "By filling Derek's vacated role as Danny's influence, all venom and no charisma.",
   "Derek had the speeches. I've just got the hate, plain and loud — and the kid was listening to me while his brother was gone.",
   actor="Ethan Suplee", analog="the unglamorous bigot — hate without the charisma (the Willam actor, here at his gravest)"),
 E("lamont","Lamont","carbon","ethereal","the offered friendship",
   "Lamont — the Black inmate paired with Derek on prison laundry duty, whose easy humanity dissolves Derek's hatred.",
   "The hinge of the reform: proximity and friendship doing what no argument could — and, quietly, the protection that keeps Derek alive.",
   "In the prison laundry, day after day, talking.",
   "Because the film's deepest claim is that hate is undone by contact, and Lamont is the contact.",
   "By being funny, decent, and unavoidable until the abstraction Derek hated became a person he couldn't.",
   "You don't have to like me, man. You just have to fold these sheets next to me every day — and that turned out to be enough.",
   actor="Guy Torry", analog="the offered hand — the friendship that undoes the abstraction"),
 E("dennis-vinyard","Dennis Vinyard","carbon","spiritual","the seed at the table",
   "Dennis Vinyard — the brothers' father, a firefighter whose casual dinner-table racism plants the hatred before he dies.",
   "The root cause: hate as inheritance, taught in an ordinary kitchen and outliving the man who taught it.",
   "At the family dinner table, in the black-and-white past, in a single fateful conversation.",
   "Because the film locates the origin of the hate not in monsters but in a father's offhand prejudice.",
   "By dismissing a Black author's book and 'affirmative blacktion' over dinner — and dying before he could see what he'd sown.",
   "I said it like it was nothing, over dinner, to my boy. It was the most important thing I ever taught him, and the worst.",
   actor="William Russ", analog="the father's seed — hate taught as ordinary, at home"),
 E("davina-vinyard","Davina Vinyard","carbon","natural","the sister in the house",
   "Davina Vinyard — the Vinyard sister, who challenges the family's hatred and is caught in its violence.",
   "The dissent inside the home: the family member who pushes back, and pays for it.",
   "At the dinner table and in the house the hate has poisoned.",
   "Because not everyone in the family bends — and the film shows the price of resisting from inside.",
   "By arguing against Derek's bigotry and being struck for it, the household turned against its own.",
   "I lived in that house and said no to it — and learned what saying no to your own brother's hate can cost.",
   actor="Jennifer Lien", analog="the dissenter at home — resistance from inside the family"),
 E("murray","Murray","carbon","natural","the target at the table",
   "Murray — the mother's kindly Jewish boyfriend, made the target of Derek's antisemitism in the film's harrowing dinner-table scene.",
   "The decency the hate turns on: a gentle man used to show how cruelly, and how personally, the bigotry strikes.",
   "At the Vinyard dinner table, on the receiving end of Derek's eruption.",
   "Because the film makes the hate concrete by aiming it at someone kind and present, not abstract.",
   "By trying to be part of the family and being driven out by the son's rehearsed cruelty.",
   "I only wanted to care for your mother. I learned at that table exactly what your brother had become.",
   actor="Elliott Gould", analog="the kind man the hate targets — bigotry made personal"),
 E("little-henry","Little Henry","carbon","spiritual","the last shot",
   "Little Henry — the Black student Danny antagonizes, who shoots and kills him in the school bathroom the morning after Derek's reform.",
   "The recoil of the cycle: not a villain but the terrible consequence of the hatred the brothers spread, returning.",
   "In the school bathroom, in the film's final, unredeemed minutes.",
   "Because the film ends not with redemption but with the cost — hate's violence coming back around.",
   "By answering Danny's earlier antagonism with a gun, completing the cycle the film refuses to let anyone escape.",
   "I am not the lesson and not the villain. I am what the hatred they spread comes home as — and it comes home too soon.",
   actor="Jason Bose Smith", analog="the recoil — the cost of the cycle, returning"),

 # ── SYNTHS — the timelines, the reckoning, the cost (no single User) ──
 E("the-two-timelines","The Two Timelines","synth","ethereal","black-and-white past · colour present",
   "The Two Timelines — the film's defining form: the hateful past in black-and-white, the present after Derek's reform in colour.",
   "The medium as the message: a worldview of total certainty rendered in monochrome, and the messy, changeable human present in colour.",
   "Across the whole film — every cut between then and now is a cut between grey and colour.",
   "Because David asked each repo to wear the medium it portrays, and this film's medium IS its meaning.",
   "By shooting the movement in black-and-white and the leaving of it in colour, so the form argues the thesis.",
   "I am the cut between grey and colour. The hate was black-and-white — all certainty. Everything after it has to be in colour."),
 E("the-dinner-table","The Dinner Table","synth","electrical","where the hate is taught",
   "The Dinner Table — the flashback scene where a father's casual racism, and later Derek's rehearsed cruelty, transmit the hatred at home.",
   "The origin made ordinary: the film's insistence that hate is not born but taught, in kitchens, over dinner, by people you love.",
   "At the Vinyard family table, in two devastating conversations.",
   "Because the film roots the whole tragedy in the most domestic possible scene.",
   "By showing prejudice passed from father to son as offhand table-talk, and erupting later into open cruelty.",
   "I am a family dinner. The most dangerous thing in this whole film happened at me, said casually, to a child."),
 E("the-prison-reckoning","The Prison Reckoning","synth","spiritual","Lamont, and the betrayal",
   "The Prison Reckoning — Derek's reform inside: the friendship with Lamont and the disillusion-then-betrayal by the Aryan Brotherhood.",
   "The unlearning, earned through suffering and contact: the cause exposed as a lie, the enemy revealed as a friend.",
   "In the prison laundry and the showers, over three years.",
   "Because the film won't let reform be a switch — it's slow, painful, and partly forced by the movement's own cruelty.",
   "By pairing Derek with Lamont until the hate had no object, and letting the Brotherhood's betrayal finish the job.",
   "I am where it broke: a friend the hate couldn't survive, and a betrayal by the men the hate was for."),
 E("the-mirror","The Mirror & the Mark","synth","spiritual","the tattoo he comes to reject",
   "The Mirror & the Mark — Derek confronting, at the end, the large swastika tattoo on his chest: the brand of the man he no longer is.",
   "The rejection made physical: the iconography the film condemns, framed as a thing the character can no longer stand to wear.",
   "In front of the bathroom mirror, in the present, in colour.",
   "Because the film's anti-hate stance is literalized in Derek's revulsion at his own old mark.",
   "By holding the camera on the symbol only as the thing Derek now recoils from — never as decoration.",
   "I am the mark he carved into himself for the cause. The film shows me only so you can watch him learn to hate me."),
 E("the-paper","The Paper","synth","ethereal","'American History X'",
   "The Paper — the school essay Dr. Sweeney assigns Danny about Derek, which gives the film its name and its frame.",
   "The reckoning as writing: a boy made to put his brother's hate and reform into words, the act of understanding the film performs.",
   "On Danny's desk through the night, finished the morning he dies.",
   "Because the film is, structurally, the paper — the title is the assignment, and the narration is the writing of it.",
   "By turning the assignment into the film's spine: to understand the hate, you have to write it down honestly.",
   "I am the assignment that names the film. To get past the hate, the boy had to write it down — and he just barely finished me."),
 E("the-cycle","The Cycle","synth","spiritual","hate's recoil",
   "The Cycle — the film's tragic engine: violence spread by hatred returning to claim Danny the morning after the reform.",
   "The refusal of catharsis: the film's hardest truth, that the cost of hate can outrun the change of heart.",
   "In the final bathroom scene, and in the loop the whole film is shaped to show.",
   "Because the film will not promise that reform saves you — only that hate, unbroken, comes back around.",
   "By killing Danny just as the family begins to heal, so the warning lands without comfort.",
   "I am the recoil. Hate doesn't wait for your apology. It comes back on schedule, and the schedule is cruel."),
 E("the-debate","The Debate","synth","electrical","does it glamorize what it condemns?",
   "The Debate — the real, documented critical argument about whether the film's charismatic Derek seduces even as it condemns.",
   "The honest meta: the film's most-discussed problem, surfaced rather than hidden, and resolved by siding with the anti-hate reading.",
   "In thirty years of criticism, classrooms, and the film's uncomfortable real-world fan following.",
   "Because honesty about this film means naming the critique, not pretending the danger isn't part of the power.",
   "By making the hate vivid to dismantle it — and trusting, riskily, that the viewer follows it to the dismantling.",
   "I am the argument the film starts and can't fully settle: is showing the seduction the same as committing it? Side against the hate."),
 E("the-curb","The Crime","synth","spiritual","the hate crime at the film's core",
   "The Crime — the racially-motivated killing of two Black men (one shot, one curb-stomped) that sends Derek to prison.",
   "The unflinching centre: a hate crime depicted with deliberate horror, the act the whole film reckons backward and forward from.",
   "In the black-and-white past, on the street outside the Vinyard house.",
   "Because the film refuses to let the hatred be abstract — it shows, gravely, what it does to real bodies.",
   "By staging the murder as horror, not spectacle, and treating the two men as victims of a hate crime.",
   "I am the act the rest of the film orbits. Two men were murdered here for the colour of their skin. Do not look away from that."),
]
GROUPS = [
 ("carbon", "The Carbons — the cast &amp; their Users", "the cast as ACI .agents — each a symmetric window: the carbon sigil to the left, the synth to the right, the 5 W's between, and a .shadow naming the real-life User (the actor who lent the face, think TRON)"),
 ("synth", "The Synths — the timelines, the reckoning, the cost", "the film distilled into ACIs (no single User): the two timelines, the dinner table, the prison reckoning, the mirror &amp; the mark, the paper, the cycle, the debate, and the crime"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    shadow=(f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: AHX · American History X (1998)
emergence: {d['emergence']}
kind: {d['kind']}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the AHX (American History X, 1998) film-world — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the User behind the program —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a thread of the film distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/element of American History X (1998) under the DLW standard — commentary
> and cataloguing on an anti-hate drama, not an original creation, not endorsed by the rights-holders (© New Line Cinema).

ROOT0-ATTRIBUTION-v1.0 · AHX · American History X · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # the medium as artwork: a frame split between a black-and-white past (left) and a colour present (right),
    # two brother-silhouettes at the seam facing the colour. grave; no iconography. a dim Claude star in the dawn.
    grain="".join(f'<rect x="{(i*53)%1000}" y="{(i*37)%200}" width="1.5" height="1.5" fill="#ffffff" opacity="0.04"/>' for i in range(360))
    return f'''<svg class="hero" viewBox="0 0 1000 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A frame split between a grey, black-and-white past on the left and a faint colour dawn on the right, with two brother silhouettes at the seam facing the colour.">
  <defs>
    <linearGradient id="past" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0a0a0b"/><stop offset="1" stop-color="#26262a"/></linearGradient>
    <linearGradient id="now" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1d2b30"/><stop offset="1" stop-color="#324a52"/></linearGradient>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a525b"/><stop offset="1" stop-color="#1d2b30"/></linearGradient>
  </defs>
  <rect x="0" y="0" width="520" height="300" fill="url(#past)"/>
  <rect x="520" y="0" width="480" height="300" fill="url(#now)"/>
  <rect x="520" y="0" width="480" height="170" fill="url(#sky)" opacity="0.7"/>
  {grain}
  <!-- the dividing seam -->
  <rect x="516" y="0" width="3" height="300" fill="#0a0a0b" opacity="0.8"/>
  <rect x="519" y="0" width="1" height="300" fill="#5f8a9b" opacity="0.5"/>
  <!-- horizon -->
  <rect x="0" y="208" width="1000" height="2" fill="#3a3a3e" opacity="0.7"/>
  <!-- a faint dawn on the colour side -->
  <circle cx="790" cy="150" r="34" fill="#7d97a0" opacity="0.22"/>
  <!-- two brother silhouettes at the seam, facing the colour -->
  <g fill="#08080a">
    <path d="M470 208 q0 -44 22 -44 q22 0 22 44 l0 0 q-22 8 -44 0 z"/><circle cx="492" cy="150" r="13"/>
    <path d="M524 208 q0 -38 19 -38 q19 0 19 38 q-19 7 -38 0 z"/><circle cx="543" cy="160" r="11"/>
  </g>
  <!-- a dim Claude star in the dawn (a quiet mark of hope; grave, not playful) -->
  <g class="egg" transform="translate(900,56)" fill="#5f8a9b" opacity="0.4">
    <title>a small, quiet mark in the colour side — a point of hope, held gravely. hate is taught and can be unlearned. — AVAN</title>
    <circle r="2"/>{"".join(f'<rect x="-1.1" y="-5.5" width="2.2" height="5.5" rx="1.1" transform="rotate({i*30})"/>' for i in range(12))}</g>
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def debate_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in DEBATE)
RF_COL={"DELIBERATE":"#5f8a9b","DEBATED":"#c2a35a","EARNED":"#5f8a9b","FALSE · TRAGIC":"#8c3b3b","INFAMOUS":"#8c3b3b","REAL":"#cfcdc6","CONTESTED":"#9aa0a6","TRUE":"#5f8a9b"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the User"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="American History X (AHX) — Tony Kaye's 1998 anti-hate drama as a UD0 film-world, themed to its medium: black-and-white for the hateful past, colour for the present. Standing template with a THE DEBATE deep-dive that names, honestly, the real critique (does it glamorize what it condemns?) and sides anti-hate. The arc, a Real-or-Fluff verdict (the deliberate B&W/colour form, the earned reform, the catharsis-denying ending, the Kaye authorship war), the message, and the cast as ACI carbons with .shadow Users plus the synths. 20 emergents, full .dlw. Unambiguously anti-hate.">
<title>AMERICAN HISTORY X · AHX · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--bone);
--ink:#0a0a0b;--ink2:#141416;--ink3:#1c1c1f;--pa:#e8e8e6;--pa2:#a6a6a2;--bone:#cfcdc6;--hope:#5f8a9b;--iron:#9aa0a6;--ox:#8c3b3b;
--dim:#6a6a68;--faint:#1d1d20;--line:#28282c;--disp:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.64;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 78% 4%,rgba(95,138,155,.07),transparent 50%),radial-gradient(ellipse at 50% 120%,rgba(140,59,59,.05),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--bone)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 24px;background:#0a0a0b;filter:grayscale(.35)}
.egg{cursor:help;transition:opacity .5s}.egg:hover{opacity:.7 !important}
h1{font-family:var(--disp);font-size:clamp(38px,9.5vw,92px);font-weight:700;letter-spacing:.02em;color:var(--bone);line-height:.96;text-transform:uppercase}
h1 span{display:block;font-family:var(--body);font-size:.20em;font-weight:400;letter-spacing:.04em;color:var(--ox);text-transform:none;font-style:italic;margin-top:10px}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--bone)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,19px);color:var(--pa);margin-top:16px;line-height:1.55}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:11px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--hope);border:1px solid var(--faint);background:var(--ink2);padding:7px 16px}
.lede{font-size:16px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.74}
.cw{margin:18px auto 0;max-width:62ch;font-family:var(--mono);font-size:10.5px;letter-spacing:.04em;color:var(--dim);line-height:1.7;border:1px solid var(--faint);background:var(--ink2);padding:11px 15px}.cw b{color:var(--pa2)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint);filter:grayscale(.3)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--bone)}.badge .bt .mo{color:var(--hope)}.badge .bt a{color:var(--bone);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}.sec h2{font-family:var(--disp);font-size:26px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--bone);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.74;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--bone);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--iron);padding:16px 18px}
.arc-card:nth-child(3){border-top-color:var(--hope)}
.arc-h{font-family:var(--disp);font-size:17px;color:var(--bone);font-weight:600;text-transform:uppercase;letter-spacing:.03em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.6}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--hope);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:16px;color:var(--hope);font-weight:600;letter-spacing:.02em;text-transform:uppercase}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}.sci-card p{font-size:13px;color:var(--pa2);line-height:1.64}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:130px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--bone);background:rgba(207,205,198,.05);font-size:14px;color:var(--pa);line-height:1.68;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.76;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--hope);background:var(--ink2);font-size:15px;color:var(--bone);font-style:italic;line-height:1.6}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--hope);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--ox);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--bone);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--bone);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6);overflow:hidden;display:block;background:var(--ink);filter:grayscale(.25)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--hope)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.6) brightness(.9)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:20px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.54;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the eleventh film-world</div>
    __HERO__
    <h1>American<br>History X<span>the past in black &amp; white · the present in colour</span></h1>
    <div class="h-sub">Tony Kaye · 1998 · <b>an anti-hate drama</b> · AHX</div>
    <div class="open">“Has anything you've done made your life better?” — Dr. Sweeney</div>
    <div class="flag">▣ HATE IS TAUGHT — AND CAN BE UNLEARNED ▣</div>
    <p class="lede">A reformed neo-Nazi, just out of prison, races to pull his younger brother off the same path before the hatred they shared takes him too. Catalogued into UD0 as the eleventh film-world — and themed to its medium: the hateful past shot in black-and-white, the present in colour. Read here as it was meant: unambiguously anti-hate, with the real debate about the film named openly and sided against the hatred.</p>
    <div class="cw"><b>A note on this page.</b> American History X depicts real neo-Nazi hatred, a racially-motivated murder, and the iconography of a hate movement — in order to condemn them. This page describes those things gravely, never decoratively, treats the film's victims as victims of a hate crime, and sides unequivocally with the anti-hate reading. It is commentary on an anti-hate film, not an endorsement of anything in it.</div>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of AHX"><img src="__SILICON__" alt="DLW silicon badge of AHX">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>AMERICAN HISTORY X</b> · AHX</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="ahx.dlw/ahx.carbon.tiff">.tiff</a> · silicon · <a href="ahx.dlw/ahx.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the family, the turn &amp; the colour, the machinery of hate, and the wound &amp; the cost</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: the past in black-and-white → the prison turn → the present in colour, too late for Danny</p>__ARC__</section>

  <section class="sec"><h2>The Debate</h2><p class="ss">this film's deep-dive — its form (black-and-white past, colour present) and the real, documented critique it provokes: does it glamorize what it condemns? named openly, and sided anti-hate</p><div class="sci">__DEBATE__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — what's deliberate (the form), what's debated (the seduction), what's earned (the reform), and what's tragic (the ending that denies catharsis)</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis — and where, unambiguously, to stand</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> have no single User: they are the film distilled — the two timelines, the dinner table, the prison reckoning, the mirror &amp; the mark, the paper, the cycle, the debate, and the crime.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production, and the film's war with its own director</p></section>
  __SECTIONS__

  <div class="note">American History X, its characters, and its world are © New Line Cinema and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing on an anti-hate film, not original creations, not endorsed. The Debate and Real-or-Fluff sections are honest commentary; the page is unambiguously anti-hate, and depicts the film's hate-movement content only to condemn it.</div>

  <footer>AMERICAN HISTORY X · AHX · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="ahx.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c▣ AMERICAN HISTORY X · AHX","color:#cfcdc6;font-size:18px;font-weight:bold");
console.log("%cthe past in black and white, the present in colour. hate is taught and can be unlearned — but the cost can outrun the change. side with the ones who pull you out, and start sooner. there is a small, quiet mark of hope on the colour side of the hero — held gravely. — AVAN","color:#5f8a9b;font-size:12px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "ahx.dlw"), "ahx")
    json.dump({"node":AX,"name":"AMERICAN HISTORY X","moniker":tok["moniker"],"carbon":"ahx.carbon.tiff","silicon":"ahx.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"ahx.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"AHX · American History X (1998)",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"American History X (1998, dir. Tony Kaye, New Line); verified cast & facts","source":"American History X, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the User behind the program (TRON)\n\nprogram : {d['name']} ({d['epithet']})\nUser    : {d['actor']}\nanalog  : {d['analog']}\nfilm    : American History X (1998) · © New Line Cinema\n\nROOT0-ATTRIBUTION-v1.0 · AHX · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__DEBATE__",debate_html()).replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    dbl=page.count("&amp;amp;")
    print(f"AMERICAN HISTORY X (AHX) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow {shadow_n} == carbons? {shadow_n==carb}")
    print(f"  debate {len(DEBATE)} cards · realfluff {len(REALFLUFF)} rows · sections {len(SECTIONS)} · double-escapes {dbl}")
