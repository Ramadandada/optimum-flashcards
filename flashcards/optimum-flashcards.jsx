import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

// ========== CARD DATA ==========
const CARDS = [
  // ===== COLD CALL =====
  { id: 1, cat: 'Cold Call', q: 'The 7 steps of a cold call door visit', a: '1) Greeting\n2) Place yourself in area\n3) Ask the magic question\n4) Get card\n5) Gather info\n6) Get gatekeeper\'s name\n7) Get out', type: 'list' },
  { id: 2, cat: 'Cold Call', q: 'The magic 11-word question at every door', a: '"Who can I contact about what you do for drinking water and ice for your employees?"', type: 'script' },
  { id: 3, cat: 'Cold Call', q: 'Why "Who can I CONTACT" instead of "who handles this"?', a: '"Contact" is future tense — it disarms the gatekeeper because it signals you\'re leaving immediately. They\'re more likely to give you the card.', type: 'concept' },
  { id: 4, cat: 'Cold Call', q: 'What do you bring with you when cold-calling a door?', a: 'A pen and a smile. Nothing else. No bag, no folder, no laptop.', type: 'concept' },
  { id: 5, cat: 'Cold Call', q: 'The "place yourself in the area" opener', a: '"I have an appointment next door at ABC Company. I\'ve been by here a million times — I figured I\'d stop in since I had a few minutes."', type: 'script' },
  { id: 6, cat: 'Cold Call', q: '5 info-gathering questions at the door (after getting the card)', a: '1) What do you do for drinking water?\n2) Do you get those 5-gallon jugs delivered?\n3) Any issues with the water?\n4) How many coolers do you have?\n5) Do you guys do anything for ice?', type: 'list' },
  { id: 7, cat: 'Cold Call', q: 'How to exit the door cleanly', a: '"Awesome — what was your name? Thanks for your help. I\'ll give [decision-maker] a call. Have a great day."', type: 'script' },
  { id: 8, cat: 'Cold Call', q: 'How do you classify cards after collecting them?', a: 'Rate 1–5. Call the 3s, 4s, 5s yourself. Pass the 1s and 2s to the telemarketer. Don\'t waste time on weak leads.', type: 'concept' },

  // ===== PHONE =====
  { id: 9, cat: 'Phone', q: 'The 4 steps of the appointment-setting phone call', a: '1) Greeting / Clear time\n2) Relevance\n3) Value proposition\n4) Assumptive close', type: 'list' },
  { id: 10, cat: 'Phone', q: 'How long should the entire phone call take?', a: '30 seconds total. Get to the point in 15–20 seconds.', type: 'concept' },
  { id: 11, cat: 'Phone', q: 'How to "clear the time" instead of asking permission', a: '"Glad I caught you. I\'ll be quick — only need a couple seconds."\n\nNEVER ask "is now a good time?" — it\'s a yes/no that invites a no.', type: 'script' },
  { id: 12, cat: 'Phone', q: 'The relevance line (using info from the door visit)', a: '"I stopped by the other day, talked to Selina up front. She said you\'re the guy that handles water and ice. She also mentioned you use 5-gallon jugs and run out sometimes — is that right?"', type: 'script' },
  { id: 13, cat: 'Phone', q: 'The value proposition line', a: '"We have systems that give you a never-ending supply of purified water — usually cost less than the jugs. Most sanitary on the market. We work with a bunch of your neighbors."', type: 'script' },
  { id: 14, cat: 'Phone', q: 'The assumptive close line', a: '"I\'m going to be next door Tuesday and Thursday — I have appointments all around you. Does Tuesday at 2 work, or is Thursday better? I just want 10 minutes of your time."', type: 'script' },
  { id: 15, cat: 'Phone', q: 'Objection — "We\'re all set."', a: '"You may be — but Sally said you don\'t actually drink the water. Most of your neighbors said the same until they saw what we do. Have you ever had Smart Water? Our machines make Smart Water. 10 minutes — Tuesday or Thursday?"', type: 'script' },
  { id: 16, cat: 'Phone', q: 'Objection — "We tried this before, didn\'t like it."', a: '"You haven\'t tried ours. Our systems are the most technologically advanced on the market. Have you ever had Smart Water? Our machines make Smart Water. Just 10 minutes — I guarantee it\'s worth your while."', type: 'script' },
  { id: 17, cat: 'Phone', q: 'Objection — "Just send me some info."', a: '"If I send info, you\'ll have more questions than answers. That\'s why I do everything in person. 10 minutes is all I need — I\'m gonna be right next door anyway."', type: 'script' },

  // ===== 10-STEP PITCH =====
  { id: 18, cat: '10-Step Pitch', q: 'List all 10 steps of the sales pitch in order', a: '1) Greeting\n2) Build rapport\n3) Gather info\n4) Go to the cooler\n5) Destroy what they have\n6) Describe units top to bottom\n7) Purification\n8) Installation\n9) Service\n10) Close for demo', type: 'list' },
  { id: 19, cat: '10-Step Pitch', q: 'Why are steps 1–3 (greeting, rapport, gather info) critical?', a: 'People buy from people. New reps skip these and lose deals. Build trust first — your goal is to make the customer your best friend in 2 minutes.', type: 'concept' },
  { id: 20, cat: '10-Step Pitch', q: 'How to transition from rapport into gathering info', a: '"Mr. Customer, before I show you what we do, let me ask you a few questions. I don\'t want to waste your time on stuff you don\'t need."', type: 'script' },
  { id: 21, cat: '10-Step Pitch', q: 'The Reverse Osmosis line — MEMORIZE EXACTLY', a: '"Are you familiar with reverse osmosis?\n\nKnown worldwide as the best way to purify drinking water."', type: 'script' },
  { id: 22, cat: '10-Step Pitch', q: 'The Smart Water line — MEMORIZE EXACTLY', a: '"Have you ever had Smart Water? Our machines make Smart Water — that\'s electrolyte-enhanced, pH-balanced water. It\'s like having a bottled water plant right in your office."', type: 'script' },
  { id: 23, cat: '10-Step Pitch', q: 'The boost filter blurb', a: '"We use a boost filter that adds calcium, magnesium, potassium, and sodium bicarbonate. Raises the pH and makes it more healthy and hydrating."', type: 'script' },
  { id: 24, cat: '10-Step Pitch', q: 'The in-tank sanitation blurb', a: '"We sanitize in-tank with activated oxygen — also called ozonation. It bubbles through and hyper-oxygenates the water. Kills 100% of bacteria, mold, slime, viruses. Nothing organic can grow in our machines."', type: 'script' },
  { id: 25, cat: '10-Step Pitch', q: 'The installation blurb', a: '"We hook up like a fridge ice maker. Lines look like cable wire — we run them up walls, over drop ceilings. Under the sink we put a brass T at the cold water shutoff. Takes my guy 20–30 minutes. 100% reversible."', type: 'script' },
  { id: 26, cat: '10-Step Pitch', q: 'The full service blurb — MEMORIZE EXACTLY', a: '"We put you on a maintenance schedule that we manage for you. Once a year we change all your filters no matter what — rated for 1,500 gallons. That\'s a lot of water.\n\nThere\'s a microprocessor monitoring filter life and water quality. If anything\'s off in between, the machine tells you. You never drink or pay for imperfect water."', type: 'script' },
  { id: 27, cat: '10-Step Pitch', q: 'The 5-day fix guarantee line', a: '"If we don\'t fix an issue within 5 days, you don\'t pay for your machine that month."', type: 'script' },
  { id: 28, cat: '10-Step Pitch', q: 'The dog-bowl line (destroying jug coolers)', a: '"Do you have a dog at home? You fill the bowl, two days later it\'s slimy and nasty — that\'s organic compounds reacting with plastic. Same thing in your water cooler tank — except people drink out of yours."', type: 'script' },
  { id: 29, cat: '10-Step Pitch', q: 'The workman\'s comp / 5-gallon jug line', a: '"60% of all workman\'s comp claims in an office environment come from these 5-gallon jugs. Average non-surgical back claim is around $100,000."', type: 'script' },
  { id: 30, cat: '10-Step Pitch', q: 'The "open system" / glug-glug line', a: '"This is what we call an open system. Hear that glug-glug-glug? That\'s outside air being pulled into the tank through the opposite spigot. Whatever\'s in the air, on people\'s hands, on the bottle — gets pulled right into the water."', type: 'script' },
  { id: 31, cat: '10-Step Pitch', q: 'The cleaning frequency line', a: '"The International Bottled Water Association says clean every 6 weeks or every other bottle change. Nobody ever does it."', type: 'script' },
  { id: 32, cat: '10-Step Pitch', q: 'The cross-contamination / workplace epidemic line', a: '"People\'s hands all over the lever, sport bottles jammed against the spigot they\'ve been drinking from for days. Viruses live on plastic 3–5 days. This is how workplace epidemics happen."', type: 'script' },
  { id: 33, cat: '10-Step Pitch', q: 'Destroying a filter cooler (carbon-only)', a: '"Carbon only removes gases — chlorine, sulfur. Same as your fridge or a Brita filter. Lead, mercury, arsenic, chromium 6 — all stay in your water. You\'re basically drinking the same as tap, except now it sat in a tank where bacteria could grow."', type: 'script' },
  { id: 34, cat: '10-Step Pitch', q: 'The 3-step close for the demo', a: '1) Make them feel special — "Because you\'re a major / because we work with so many of your neighbors, we offer a free trial."\n2) "If you were to do a free trial, would this be the best spot — or somewhere else?"\n3) "Which machine would you like to try?"', type: 'list' },
  { id: 35, cat: '10-Step Pitch', q: 'How to NOT close for the demo (yes/no trap)', a: 'NEVER ask "Do you want to do a free trial?" — that\'s a yes/no question that invites a no.\n\nAlways ask "WHICH machine would you like to try?" — assumes the trial is happening.', type: 'concept' },

  // ===== CLOSING & PAPERWORK =====
  { id: 36, cat: 'Closing', q: 'The two-day follow-up opening line', a: '"Hey, I was right next door for another appointment. We put a machine in a couple days ago — figured I\'d pop in. How\'d my technician do? Did he keep it clean in here?"', type: 'script' },
  { id: 37, cat: 'Closing', q: 'The MAGIC transition line — from chitchat to the close', a: '"Sounds like you\'re gonna keep it. As the next step, I just need to grab a signature to set up your account."', type: 'script' },
  { id: 38, cat: 'Closing', q: '"Follow the Pen" — the 5-point sequence on Page 2', a: '1) Customer info → "Here\'s your info."\n2) Price → "$115 a month."\n3) Billing frequency → "We\'ll bill you monthly."\n4) Term → "We guarantee your price for 60 months."\n5) Install fee → "One-time $275 install fee. Sign there. Flip when done."', type: 'list' },
  { id: 39, cat: 'Closing', q: 'WHY sandwich the term between price and install fee?', a: 'If they push back, it\'ll be on the install fee (the LAST thing you said) — way easier to handle than fighting term.\n\nThe sandwich hides the 60-month commitment between two friendlier numbers.', type: 'concept' },
  { id: 40, cat: 'Closing', q: 'How to respond to "60 months is too long"', a: '"60 months is our standard term."\n\nThen SHUT UP. Let them talk to themselves.\n\nOnly if they keep pushing: "These machines are extremely expensive — we typically don\'t break even until 30–36 months. That\'s why."', type: 'script' },
  { id: 41, cat: 'Closing', q: 'The 4 negotiation levers in priority order', a: '1) Waive install fee (costs you $75)\n2) Offer free month rebate ($0 cost to you — only on 36+ mo, credit-approved)\n3) Drop term to 36 months (costs 2x multiplier — last resort)\n4) Drop price (costs you bonus eligibility)', type: 'list' },
  { id: 42, cat: 'Closing', q: 'The referral ask AFTER they sign', a: '"By the way — we have a $50 referral bonus per machine. Any other locations? Family members with businesses? Anyone you think I should give a call to?"', type: 'script' },
  { id: 43, cat: 'Closing', q: 'The Customer Satisfaction Guarantee summary (Page 1)', a: '"Sign there, I\'ll tell you what it says: Everything\'s included — filters, maintenance, service, parts. If we don\'t fix an issue in 5 days, you don\'t pay for your machine that month. Pretty cool, huh? Flip when done."', type: 'script' },
  { id: 44, cat: 'Closing', q: 'The Page 3 sneaky trick (multi-unit deals)', a: 'When they\'re sign-and-flipping mindlessly, say:\n\n"This is delivery and acceptance — just a permission slip for me to install the rest of your machines. Sign there."\n\n(Saves you a second trip. Harmless because we can\'t fund until everything\'s installed anyway.)', type: 'script' },
  { id: 45, cat: 'Closing', q: 'Which line on Terms & Conditions can NEVER be struck?', a: 'Line 8 — Early Termination.\n\nIf they strike this, the contract becomes month-to-month and the deal economics break. You\'ll be charged 2x commission AND 2x bonus back. They could fire you.', type: 'concept' },
  { id: 46, cat: 'Closing', q: 'Which Terms line CAN they strike?', a: 'Line 9 — Auto-renewal.\n\nThey can opt out of the 12-month auto-renew. We don\'t care — it just goes month-to-month after the term ends.', type: 'concept' },

  // ===== COMP PLAN =====
  { id: 47, cat: 'Comp Plan', q: 'Term multipliers — memorize all 5', a: '60 months = 5x\n48 months = 4x\n36 months = 3x\n24 months = 2x\n12 mo / month-to-month / credit declined = 1x', type: 'list' },
  { id: 48, cat: 'Comp Plan', q: 'Average commission per unit (the math)', a: '~$140/mo (avg price) × 4x (avg term multiplier) = ~$560 per unit\n\nQuota of 12 units × $560 = ~$6,720/mo in base commission', type: 'concept' },
  { id: 49, cat: 'Comp Plan', q: 'The 3 quarterly bonus tiers', a: 'Tier 1: $4,250 monthly RMR → $8,500/qtr bonus floor\nTier 2: $5,701 monthly RMR → $17,000/qtr bonus floor\nTier 3: $7,000 monthly RMR → $28,000/qtr bonus floor\n\nThis is ON TOP of regular commission.', type: 'list' },
  { id: 50, cat: 'Comp Plan', q: 'Prime Minister\'s Club', a: '250 units sold in a calendar year = $7,000 cash bonus.', type: 'concept' },
  { id: 51, cat: 'Comp Plan', q: 'His Majesty\'s Circle', a: '150+ units sold in a year = all-expenses-paid trip for two with the company. (US version: Ambassador\'s Club.)', type: 'concept' },
  { id: 52, cat: 'Comp Plan', q: 'Install fee commission tiers', a: 'Charge $275 = $100 to you (CA — system shows $75, that\'s a glitch)\nCharge $225 = $80 to you\nCharge $175 = $0 (break even)\nBelow $150 = -$75 (you PAY)\n\nAlways charge full $275 when you can.', type: 'list' },
  { id: 53, cat: 'Comp Plan', q: 'Daily quota math', a: '20 doors/day → 100/week\n2-3% become free trials → 8-12 trials/month\n~1.5 units per deal × 8 deals = 12 units = quota\nSet 1-2 appointments/day → 32/qtr (matches the quarterly minimum)', type: 'list' },
  { id: 54, cat: 'Comp Plan', q: 'Renewals and Upgrades commission', a: 'Renewals: 50% commission, NO bonus\nUpgrades: 50% of price difference, NO bonus, NO quota credit\n\n(Upgrades cost the company so much you may not even be allowed to do them.)', type: 'concept' },

  // ===== PRODUCTS =====
  { id: 55, cat: 'Products', q: 'PW-50 specs', a: '$85/mo CAD\n1.8 gal cold ready\nHot + cold (NO room temp, NO ice)\nNOT touch-free\nDrip drain only\nGood for: 15-20 employees', type: 'list' },
  { id: 56, cat: 'Products', q: 'PW-70 specs', a: '$105/mo CAD\n2.3 gal cold ready\nHot + cold\nTouch-free ✓\nActive drain available (+$15)\nGood for: 20-30 employees', type: 'list' },
  { id: 57, cat: 'Products', q: 'PW-90 specs (the bread and butter)', a: '$115/mo CAD\n3 gal cold ready\nHot + cold\nTouch-free ✓\nActive drain available (+$15)\nGood for: 30-40 employees\n\nThis is your default water-only pitch.', type: 'list' },
  { id: 58, cat: 'Products', q: 'PW-90 Countertop specs', a: '$95/mo CAD\nOnly 1 gal cold (small tank)\nHot + cold\nTouch-free ✓\nNO active drain available\nGood for: 15-20 employees\n\nUse only when there\'s no floor space.', type: 'list' },
  { id: 59, cat: 'Products', q: 'I-14 specs (the moneymaker)', a: '$199/mo CAD\nIce + hot + cold + room temp\n13 lb ice ready / 45 lb/day (bullet ice)\nTouch-free ✓\nALWAYS comes with active drain\n5+ gallons of water at the ready\nGood for: 40-50 employees', type: 'list' },
  { id: 60, cat: 'Products', q: 'Which 2 machines do you ALWAYS pitch?', a: 'I-14 first (ice + water) — even if they say no ice initially.\nThen the PW-90 (water only).\n\nDon\'t list every machine. Just these two.', type: 'concept' },
  { id: 61, cat: 'Products', q: 'What does the "+" mean on a model number (PW90R+)?', a: 'With boost filter (the one that adds electrolytes and raises pH).\n\nALWAYS order the + version. Without it, customer doesn\'t get Smart Water.', type: 'concept' },
  { id: 62, cat: 'Products', q: 'Cold and hot water temperatures', a: 'Cold: 3°C (~38°F)\nHot: 85°C (~185°F)\n\nGreat for tea, oatmeal, soup, ramen.', type: 'concept' },
  { id: 63, cat: 'Products', q: 'How many gallons per day does each RO membrane make?', a: '80 GPD per membrane.\n\nXL1 has TWO membranes side-by-side = 160 GPD (working in parallel, not in series).', type: 'concept' },
  { id: 64, cat: 'Products', q: 'Filter ratings', a: 'Sediment / GAC / Carbon Block: 1,500 gallons\nRO membrane: 3,000 gallons\nBoost filter: 1,500 gallons\n\nWe come once a year and change them all anyway.', type: 'concept' },
  { id: 65, cat: 'Products', q: 'The complete filtration stack (in order)', a: '1) Sediment filter (10 microns)\n2) GAC carbon filter (5 microns)\n3) Carbon block (1 micron)\n4) RO membrane (0.0001 micron)\n5) Boost filter (adds electrolytes, raises pH)', type: 'list' },
  { id: 66, cat: 'Products', q: 'XL1 — when to pitch it', a: 'High-volume locations: gyms, big offices, busy cafeterias, schools.\n\nHas TWO RO membranes (160 GPD), 5 gal cold, 2.5 gal ambient, 1.1 gal hot. LED UV sanitation. Touch-free.', type: 'concept' },
  { id: 67, cat: 'Products', q: 'What\'s special about the S4 (sparkling)?', a: 'NO reverse osmosis — sparkling needs TDS in the water for CO2 to bond. So just sediment + carbon + carbon block (no RO, no boost filter).', type: 'concept' },

  // ===== WATER SCIENCE =====
  { id: 68, cat: 'Water Science', q: 'What does TDS stand for?', a: 'Total Dissolved Solids.\n\nMeasures everything dissolved in water — heavy metals, chemicals, minerals — except gases.', type: 'concept' },
  { id: 69, cat: 'Water Science', q: 'TDS chart — memorize the buckets', a: '<20 PPM = pure / RO water\n<50 PPM = high-quality bottled\n80-450 PPM = municipal tap\n170+ PPM = hard water\n300+ PPM = high TDS, don\'t drink\n500 PPM = max contaminant level', type: 'list' },
  { id: 70, cat: 'Water Science', q: 'Filtration vs Purification', a: 'FILTRATION (carbon, microfiltration): removes gases like chlorine and sulfur, some particles. Down to ~1 micron.\n\nPURIFICATION (reverse osmosis): strips EVERYTHING down to 0.0001 micron — 1000x better.', type: 'concept' },
  { id: 71, cat: 'Water Science', q: 'IOCs vs VOCs', a: 'IOCs = Inorganic (non-living): lead, mercury, arsenic, chromium 6, fluoride, nitrate. RO removes these.\n\nVOCs = Organic (chemical): solvents, herbicides, pesticides. CARBON removes these.', type: 'concept' },
  { id: 72, cat: 'Water Science', q: 'PFAs — what are they?', a: '"Forever chemicals." Never leave your body. Linked to chronic illness and cancer.\n\nDow Chemical lost a multi-billion dollar lawsuit over PFAs in water.', type: 'concept' },
  { id: 73, cat: 'Water Science', q: 'Why does pure water need a boost filter?', a: 'After RO, water is acidic (~5.5-6 pH). An acidic body is more disease-susceptible.\n\nBoost filter adds calcium/magnesium/potassium/sodium bicarbonate → raises pH → alkaline = healthy.', type: 'concept' },
  { id: 74, cat: 'Water Science', q: 'How does activated oxygen (O3) work?', a: 'Air passes over an electrically charged corona wire — O2 becomes O3. The extra oxygen atom hyper-oxygenates the water.\n\nKills 100% of bacteria, mold, slime, viruses. Nothing organic can grow in oxygenated water. Doesn\'t lose effectiveness.', type: 'concept' },
  { id: 75, cat: 'Water Science', q: 'Why are TRADITIONAL UV bulbs actually BAD?', a: 'They get covered in algae and dim over time. They become a HEAT SOURCE for bacteria — opposite effect.\n\nLED UV is fine (8-year life, no dimming). Traditional bulbs are competitor weakness.', type: 'concept' },
  { id: 76, cat: 'Water Science', q: 'The 4 dissolved solids to name to a customer', a: 'Lead, mercury, arsenic, chromium 6.\n\nMemorize these — they roll off the tongue and instantly disgust the customer.', type: 'list' },

  // ===== PROCESS & TOOLS =====
  { id: 77, cat: 'Process', q: 'The 15-step complete sales process', a: '1) Hit door, get card\n2) Phone to set appointment\n3) Create Company in Water Desk\n4) Add Contact\n5) Create Meeting\n6) Run pitch, get free trial\n7) Create Opportunity\n8) Create Work Order (with 3 photos)\n9) Email scheduling@\n10) Email customer install date\n11) Install happens\n12) Two-day follow-up in person\n13) Set PCM if needed\n14) Close, scan to admin@\n15) Mark Closed Won', type: 'list' },
  { id: 78, cat: 'Process', q: 'The 3 photos to take at every free trial', a: '1) Where the cooler will go (close-up of placement spot)\n2) Under the sink (cold water shutoff)\n3) Wide shot showing the path between sink and cooler', type: 'list' },
  { id: 79, cat: 'Process', q: 'Email to scheduling — exact format', a: 'TO: scheduling@drinkoptimum.com\nCC: your manager\nSUBJECT: Install Date Request\nBODY: [Company Name] + [URL to the work order]\n\n+ any special timing requests from customer', type: 'list' },
  { id: 80, cat: 'Process', q: 'Email to admin — exact format', a: 'TO: admin@drinkoptimum.com\nSUBJECT: [Company Name] Agreement\nBODY: brief note + scanned PDF of agreement attached\n\nUse TurboScan or Notes to scan from your phone.', type: 'list' },
  { id: 81, cat: 'Process', q: 'Water Desk — top tabs vs bottom tabs rule', a: 'TOP TABS = main pages for the whole company database. DON\'T use these mid-flow.\n\nBOTTOM TABS (inside an account) = add things to that account. ALWAYS use these.', type: 'concept' },
  { id: 82, cat: 'Process', q: 'Water Desk new account — order of creation', a: '1) Companies → New Company (status: Prospect)\n2) Inside account → Contacts → New\n3) Inside account → Meetings → New (type: Self-Generated Appointment)\n\nEACH ONE BUILDS ON THE LAST. Order matters.', type: 'list' },
  { id: 83, cat: 'Process', q: 'After getting a free trial — what 2 things do you create?', a: '1) Opportunity (always check "credit requested")\n2) Work Order (link to the opportunity, attach 3 photos)\n\nThen copy work order URL → email scheduling.', type: 'list' },
  { id: 84, cat: 'Process', q: 'Water Desk search trick', a: 'Use ASTERISK for partial match.\n\nExample: "52 D*" finds all addresses starting with "52 D" — useful when you don\'t know the exact street name.', type: 'concept' },
  { id: 85, cat: 'Process', q: 'Daily CADS log', a: 'Cards (collected) + Appointments (set) + Demos (got) + Sales (made)\n\nLog every day. CADS counts deals, not units — 3 free trials at one company = 1 demo.', type: 'concept' },
  { id: 86, cat: 'Process', q: 'When do you do the two-day follow-up?', a: 'In person, UNANNOUNCED, exactly 2 days after the install.\n\nNot phone. The face-to-face triples your close rate.', type: 'concept' },

  // ===== MINDSET =====
  { id: 87, cat: 'Mindset', q: 'Why never pitch at the door?', a: '75% lower close rate.\n\nIf the customer doesn\'t INVITE you in, they psychologically resist buying. Set the appointment, get invited, pitch then.', type: 'concept' },
  { id: 88, cat: 'Mindset', q: 'The volume mantra', a: '"Volume of accounts fixes all woes."\n\nIf you only have 2 deals working and lose one, you\'re cooked. Always be hitting doors. 20/day, no excuses.', type: 'concept' },
  { id: 89, cat: 'Mindset', q: 'Always set the next step on...', a: 'YOUR schedule, not theirs.\n\n"I\'ll be in your area Tuesday at 2." — NOT — "Call me when you\'re ready."\n\nCustomers will drag deals out forever if you let them.', type: 'concept' },
  { id: 90, cat: 'Mindset', q: 'How to handle "we want to think about it"', a: '"Totally — that\'s why we offer free trials. No paperwork, no obligation. Worst case, you get amazing water for two weeks free. Which machine would you like to try?"\n\nReframe thinking-time as trial-time.', type: 'script' },
];

const CATEGORIES = ['All', 'Cold Call', 'Phone', '10-Step Pitch', 'Closing', 'Comp Plan', 'Products', 'Water Science', 'Process', 'Mindset'];

// ========== MAIN APP ==========
export default function App() {
  const [states, setStates] = useState({}); // { cardId: 'mastered' | 'drill' | undefined }
  const [activeCat, setActiveCat] = useState('All');
  const [mode, setMode] = useState('all'); // 'all' | 'drill' | 'new'
  const [shuffled, setShuffled] = useState(false);
  const [position, setPosition] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [showStats, setShowStats] = useState(false);
  const [loading, setLoading] = useState(true);

  // Load states from storage
  useEffect(() => {
    (async () => {
      try {
        const result = await window.storage.get('card-states');
        if (result?.value) setStates(JSON.parse(result.value));
      } catch (e) { /* not found, that's fine */ }
      setLoading(false);
    })();
  }, []);

  // Persist states
  const persistStates = useCallback(async (next) => {
    try {
      await window.storage.set('card-states', JSON.stringify(next));
    } catch (e) { console.error(e); }
  }, []);

  // Filtered + ordered card list
  const deck = useMemo(() => {
    let pool = activeCat === 'All' ? CARDS : CARDS.filter(c => c.cat === activeCat);
    if (mode === 'drill') pool = pool.filter(c => states[c.id] === 'drill');
    if (mode === 'new') pool = pool.filter(c => !states[c.id]);
    if (shuffled) {
      const arr = [...pool];
      for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }
      return arr;
    }
    return pool;
  }, [activeCat, mode, shuffled, states]);

  // Reset position when filter changes
  useEffect(() => {
    setPosition(0);
    setRevealed(false);
  }, [activeCat, mode, shuffled]);

  const card = deck[position];

  const mark = useCallback((status) => {
    if (!card) return;
    const next = { ...states };
    if (status === null) delete next[card.id];
    else next[card.id] = status;
    setStates(next);
    persistStates(next);
    setRevealed(false);
    setPosition(p => (p + 1 < deck.length ? p + 1 : 0));
  }, [card, states, deck.length, persistStates]);

  const skip = useCallback(() => {
    setRevealed(false);
    setPosition(p => (p + 1 < deck.length ? p + 1 : 0));
  }, [deck.length]);

  const back = useCallback(() => {
    setRevealed(false);
    setPosition(p => (p > 0 ? p - 1 : deck.length - 1));
  }, [deck.length]);

  // Keyboard shortcuts
  useEffect(() => {
    const onKey = (e) => {
      if (e.key === ' ') { e.preventDefault(); setRevealed(r => !r); }
      else if (e.key === '1') mark('mastered');
      else if (e.key === '2') mark('drill');
      else if (e.key === '3') skip();
      else if (e.key === 'ArrowLeft') back();
      else if (e.key === 'ArrowRight') skip();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [mark, skip, back]);

  // Stats
  const stats = useMemo(() => {
    const pool = activeCat === 'All' ? CARDS : CARDS.filter(c => c.cat === activeCat);
    const mastered = pool.filter(c => states[c.id] === 'mastered').length;
    const drill = pool.filter(c => states[c.id] === 'drill').length;
    const fresh = pool.filter(c => !states[c.id]).length;
    return { total: pool.length, mastered, drill, fresh };
  }, [activeCat, states]);

  const overallStats = useMemo(() => {
    const mastered = CARDS.filter(c => states[c.id] === 'mastered').length;
    return { mastered, total: CARDS.length, pct: Math.round((mastered / CARDS.length) * 100) };
  }, [states]);

  const catStats = useMemo(() => {
    return CATEGORIES.filter(c => c !== 'All').map(cat => {
      const pool = CARDS.filter(c => c.cat === cat);
      const mastered = pool.filter(c => states[c.id] === 'mastered').length;
      return { cat, mastered, total: pool.length, pct: Math.round((mastered / pool.length) * 100) };
    });
  }, [states]);

  if (loading) {
    return (
      <div style={styles.loading}>
        <div style={styles.loadingText}>OPTIMUM</div>
      </div>
    );
  }

  return (
    <div style={styles.root}>
      <style>{globalCSS}</style>

      {/* HEADER */}
      <header style={styles.header}>
        <div style={styles.brand}>
          <div style={styles.brandTop}>OPTIMUM</div>
          <div style={styles.brandSub}>SALES BIBLE · DRILL</div>
        </div>
        <button style={styles.statsBtn} onClick={() => setShowStats(true)}>
          <span style={styles.pctBig}>{overallStats.pct}%</span>
          <span style={styles.pctLabel}>{overallStats.mastered}/{overallStats.total}</span>
        </button>
      </header>

      {/* CATEGORY CHIPS */}
      <div style={styles.chipsWrap}>
        <div style={styles.chips}>
          {CATEGORIES.map(c => (
            <button
              key={c}
              onClick={() => setActiveCat(c)}
              style={{
                ...styles.chip,
                ...(activeCat === c ? styles.chipActive : {})
              }}
            >
              {c}
            </button>
          ))}
        </div>
      </div>

      {/* MODE TOGGLES */}
      <div style={styles.modes}>
        <div style={styles.modeGroup}>
          {[
            { v: 'all', l: 'ALL' },
            { v: 'drill', l: 'DRILL' },
            { v: 'new', l: 'NEW' }
          ].map(m => (
            <button
              key={m.v}
              onClick={() => setMode(m.v)}
              style={{ ...styles.modeBtn, ...(mode === m.v ? styles.modeBtnActive : {}) }}
            >
              {m.l}
            </button>
          ))}
        </div>
        <button
          onClick={() => setShuffled(s => !s)}
          style={{ ...styles.shuffleBtn, ...(shuffled ? styles.shuffleActive : {}) }}
        >
          ↯ {shuffled ? 'SHUFFLED' : 'IN ORDER'}
        </button>
      </div>

      {/* PROGRESS BAR */}
      <div style={styles.progressWrap}>
        <div style={styles.progressBar}>
          <div style={{ ...styles.progressFill, width: `${stats.total ? ((position + 1) / stats.total) * 100 : 0}%` }} />
        </div>
        <div style={styles.progressMeta}>
          <span>{deck.length ? position + 1 : 0} / {deck.length}</span>
          <span style={styles.progressDot}>·</span>
          <span style={{ color: '#6FCF97' }}>{stats.mastered} mastered</span>
          <span style={styles.progressDot}>·</span>
          <span style={{ color: '#E0A93C' }}>{stats.drill} drill</span>
          <span style={styles.progressDot}>·</span>
          <span style={{ color: '#9C9489' }}>{stats.fresh} new</span>
        </div>
      </div>

      {/* CARD AREA */}
      <main style={styles.main}>
        {deck.length === 0 ? (
          <div style={styles.emptyState}>
            <div style={styles.emptyHeadline}>No cards in this view.</div>
            <div style={styles.emptyHint}>
              {mode === 'drill' ? 'You have nothing flagged for drilling. Switch to ALL or NEW.' :
               mode === 'new' ? 'Everything in this category has been touched. Switch to ALL.' :
               'Try a different category.'}
            </div>
          </div>
        ) : (
          <AnimatePresence mode="wait">
            <motion.div
              key={card.id + '-' + revealed}
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -12 }}
              transition={{ duration: 0.18, ease: 'easeOut' }}
              style={styles.card}
              onClick={() => !revealed && setRevealed(true)}
            >
              <div style={styles.cardHeader}>
                <span style={styles.cardCat}>{card.cat}</span>
                <span style={styles.cardId}>#{String(card.id).padStart(2, '0')}</span>
              </div>

              <div style={styles.cardBody}>
                {!revealed ? (
                  <>
                    <div style={styles.cardLabel}>PROMPT</div>
                    <div style={styles.cardQuestion}>{card.q}</div>
                    <div style={styles.tapHint}>tap to reveal · or press <kbd style={styles.kbd}>space</kbd></div>
                  </>
                ) : (
                  <>
                    <div style={styles.cardLabel}>{card.type === 'script' ? 'SAY THIS' : card.type === 'list' ? 'KNOW THIS' : 'ANSWER'}</div>
                    <div style={card.type === 'script' ? styles.cardAnswerScript : styles.cardAnswer}>
                      {card.a}
                    </div>
                  </>
                )}
              </div>

              {/* status indicator */}
              {states[card.id] && (
                <div style={{
                  ...styles.statusIndicator,
                  background: states[card.id] === 'mastered' ? '#6FCF97' : '#E0A93C'
                }} />
              )}
            </motion.div>
          </AnimatePresence>
        )}
      </main>

      {/* ACTION BUTTONS */}
      {deck.length > 0 && (
        <div style={styles.actions}>
          {!revealed ? (
            <>
              <button style={styles.actBack} onClick={back}>← BACK</button>
              <button style={styles.actReveal} onClick={() => setRevealed(true)}>
                REVEAL <span style={styles.kbdLight}>SPACE</span>
              </button>
              <button style={styles.actSkip} onClick={skip}>SKIP →</button>
            </>
          ) : (
            <>
              <button style={styles.actDrill} onClick={() => mark('drill')}>
                <span style={styles.actNum}>2</span>
                <span>NEED DRILL</span>
              </button>
              <button style={styles.actMaster} onClick={() => mark('mastered')}>
                <span style={styles.actNum}>1</span>
                <span>GOT IT</span>
              </button>
              <button style={styles.actSkipSm} onClick={skip}>
                <span style={styles.actNum}>3</span>
                <span>SKIP</span>
              </button>
            </>
          )}
        </div>
      )}

      {/* STATS PANEL */}
      <AnimatePresence>
        {showStats && (
          <>
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              style={styles.overlay}
              onClick={() => setShowStats(false)}
            />
            <motion.div
              initial={{ x: '100%' }}
              animate={{ x: 0 }}
              exit={{ x: '100%' }}
              transition={{ type: 'spring', damping: 30, stiffness: 250 }}
              style={styles.statsPanel}
            >
              <div style={styles.statsHeader}>
                <div>
                  <div style={styles.statsTitle}>YOUR PROGRESS</div>
                  <div style={styles.statsSubtitle}>by category</div>
                </div>
                <button style={styles.closeBtn} onClick={() => setShowStats(false)}>✕</button>
              </div>

              <div style={styles.statsBigPct}>
                <div style={styles.statsBigNum}>{overallStats.pct}<span style={styles.statsPctSym}>%</span></div>
                <div style={styles.statsBigLabel}>OVERALL · {overallStats.mastered} of {overallStats.total} cards</div>
              </div>

              <div style={styles.catList}>
                {catStats.map(c => (
                  <div key={c.cat} style={styles.catRow}>
                    <div style={styles.catRowTop}>
                      <span style={styles.catName}>{c.cat}</span>
                      <span style={styles.catCount}>{c.mastered}/{c.total}</span>
                    </div>
                    <div style={styles.catBar}>
                      <div style={{ ...styles.catBarFill, width: `${c.pct}%` }} />
                    </div>
                  </div>
                ))}
              </div>

              <button
                style={styles.resetBtn}
                onClick={() => {
                  if (confirm('Reset all progress? This cannot be undone.')) {
                    setStates({});
                    persistStates({});
                  }
                }}
              >
                RESET ALL PROGRESS
              </button>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}

// ========== STYLES ==========
const globalCSS = `
  @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Manrope:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Manrope', sans-serif;
    background: #0F0E0C;
    color: #F0EBE0;
    -webkit-font-smoothing: antialiased;
    overscroll-behavior: none;
  }

  button {
    font-family: inherit;
    cursor: pointer;
    border: none;
    outline: none;
    -webkit-tap-highlight-color: transparent;
  }

  button:focus-visible {
    outline: 1px solid #D4A24C;
    outline-offset: 2px;
  }
`;

const styles = {
  root: {
    minHeight: '100vh',
    maxWidth: '720px',
    margin: '0 auto',
    padding: '20px 16px 120px',
    display: 'flex',
    flexDirection: 'column',
    gap: '16px',
    position: 'relative',
  },
  loading: {
    height: '100vh',
    background: '#0F0E0C',
    color: '#D4A24C',
    display: 'grid',
    placeItems: 'center',
    fontFamily: 'Fraunces, serif',
  },
  loadingText: {
    fontSize: '32px',
    letterSpacing: '0.4em',
    fontWeight: 600,
  },

  // header
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingBottom: '4px',
    borderBottom: '1px solid #2A2620',
  },
  brand: {
    display: 'flex',
    flexDirection: 'column',
  },
  brandTop: {
    fontFamily: 'Fraunces, serif',
    fontSize: '24px',
    fontWeight: 600,
    letterSpacing: '0.18em',
    color: '#D4A24C',
    lineHeight: 1,
  },
  brandSub: {
    fontFamily: 'JetBrains Mono, monospace',
    fontSize: '9px',
    letterSpacing: '0.3em',
    color: '#6B645A',
    marginTop: '4px',
  },
  statsBtn: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'flex-end',
    background: 'transparent',
    color: '#F0EBE0',
    padding: '4px 0',
    fontFamily: 'JetBrains Mono, monospace',
  },
  pctBig: {
    fontSize: '20px',
    fontWeight: 600,
    color: '#D4A24C',
    letterSpacing: '0.05em',
    fontFamily: 'Fraunces, serif',
  },
  pctLabel: {
    fontSize: '9px',
    color: '#6B645A',
    letterSpacing: '0.2em',
    marginTop: '2px',
  },

  // chips
  chipsWrap: {
    overflowX: 'auto',
    overflowY: 'hidden',
    margin: '0 -16px',
    padding: '0 16px',
    WebkitOverflowScrolling: 'touch',
    scrollbarWidth: 'none',
  },
  chips: {
    display: 'flex',
    gap: '6px',
    paddingBottom: '4px',
    minWidth: 'min-content',
  },
  chip: {
    padding: '8px 14px',
    background: 'transparent',
    color: '#9C9489',
    border: '1px solid #2A2620',
    borderRadius: '999px',
    fontSize: '11px',
    fontWeight: 600,
    letterSpacing: '0.1em',
    textTransform: 'uppercase',
    whiteSpace: 'nowrap',
    transition: 'all 0.15s',
  },
  chipActive: {
    background: '#D4A24C',
    color: '#0F0E0C',
    borderColor: '#D4A24C',
  },

  // modes
  modes: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    gap: '8px',
  },
  modeGroup: {
    display: 'flex',
    background: '#1A1814',
    padding: '4px',
    borderRadius: '8px',
    border: '1px solid #2A2620',
  },
  modeBtn: {
    padding: '6px 14px',
    background: 'transparent',
    color: '#6B645A',
    fontSize: '10px',
    fontWeight: 700,
    letterSpacing: '0.18em',
    fontFamily: 'JetBrains Mono, monospace',
    borderRadius: '5px',
    transition: 'all 0.15s',
  },
  modeBtnActive: {
    background: '#0F0E0C',
    color: '#F0EBE0',
    boxShadow: '0 1px 0 0 rgba(255,255,255,0.04)',
  },
  shuffleBtn: {
    padding: '8px 14px',
    background: '#1A1814',
    color: '#6B645A',
    fontSize: '10px',
    fontWeight: 700,
    letterSpacing: '0.18em',
    fontFamily: 'JetBrains Mono, monospace',
    borderRadius: '8px',
    border: '1px solid #2A2620',
  },
  shuffleActive: {
    color: '#D4A24C',
    borderColor: '#3A3328',
  },

  // progress
  progressWrap: {
    display: 'flex',
    flexDirection: 'column',
    gap: '6px',
  },
  progressBar: {
    height: '2px',
    background: '#1A1814',
    borderRadius: '1px',
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    background: 'linear-gradient(90deg, #D4A24C, #E0BC6E)',
    transition: 'width 0.3s ease',
  },
  progressMeta: {
    display: 'flex',
    flexWrap: 'wrap',
    alignItems: 'center',
    gap: '6px',
    fontSize: '10px',
    fontFamily: 'JetBrains Mono, monospace',
    color: '#9C9489',
    letterSpacing: '0.05em',
  },
  progressDot: {
    color: '#3A3328',
  },

  // card
  main: {
    flex: 1,
    display: 'flex',
    alignItems: 'stretch',
    minHeight: '380px',
  },
  card: {
    flex: 1,
    background: '#1A1814',
    border: '1px solid #2A2620',
    borderRadius: '4px',
    padding: '32px 28px',
    display: 'flex',
    flexDirection: 'column',
    cursor: 'pointer',
    position: 'relative',
    transition: 'border-color 0.15s',
  },
  cardHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '24px',
    fontFamily: 'JetBrains Mono, monospace',
    fontSize: '10px',
    letterSpacing: '0.2em',
    color: '#6B645A',
    fontWeight: 600,
  },
  cardCat: {
    color: '#D4A24C',
  },
  cardId: {},
  cardBody: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
  },
  cardLabel: {
    fontFamily: 'JetBrains Mono, monospace',
    fontSize: '9px',
    letterSpacing: '0.3em',
    color: '#6B645A',
    marginBottom: '16px',
    fontWeight: 600,
  },
  cardQuestion: {
    fontFamily: 'Fraunces, serif',
    fontSize: '24px',
    fontWeight: 500,
    lineHeight: 1.3,
    color: '#F0EBE0',
    letterSpacing: '-0.01em',
  },
  cardAnswer: {
    fontFamily: 'Manrope, sans-serif',
    fontSize: '17px',
    lineHeight: 1.6,
    color: '#F0EBE0',
    whiteSpace: 'pre-line',
    fontWeight: 400,
  },
  cardAnswerScript: {
    fontFamily: 'Fraunces, serif',
    fontSize: '20px',
    lineHeight: 1.45,
    color: '#F0EBE0',
    whiteSpace: 'pre-line',
    fontStyle: 'italic',
    fontWeight: 400,
    paddingLeft: '14px',
    borderLeft: '2px solid #D4A24C',
  },
  tapHint: {
    fontFamily: 'JetBrains Mono, monospace',
    fontSize: '10px',
    color: '#6B645A',
    marginTop: '32px',
    letterSpacing: '0.1em',
  },
  kbd: {
    background: '#0F0E0C',
    border: '1px solid #2A2620',
    padding: '2px 6px',
    borderRadius: '3px',
    fontFamily: 'JetBrains Mono, monospace',
    fontSize: '9px',
    color: '#9C9489',
    margin: '0 2px',
  },
  kbdLight: {
    background: 'rgba(15, 14, 12, 0.4)',
    padding: '2px 6px',
    borderRadius: '3px',
    fontFamily: 'JetBrains Mono, monospace',
    fontSize: '9px',
    marginLeft: '8px',
    letterSpacing: '0.1em',
  },
  statusIndicator: {
    position: 'absolute',
    top: 0,
    right: 0,
    width: '4px',
    height: '40px',
    borderRadius: '0 4px 0 0',
  },

  // empty state
  emptyState: {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '60px 20px',
    textAlign: 'center',
  },
  emptyHeadline: {
    fontFamily: 'Fraunces, serif',
    fontSize: '20px',
    color: '#9C9489',
    marginBottom: '8px',
    fontStyle: 'italic',
  },
  emptyHint: {
    fontSize: '13px',
    color: '#6B645A',
  },

  // actions
  actions: {
    position: 'fixed',
    bottom: 0,
    left: 0,
    right: 0,
    background: 'linear-gradient(180deg, transparent, #0F0E0C 30%)',
    padding: '40px 16px 20px',
    display: 'flex',
    gap: '8px',
    maxWidth: '720px',
    margin: '0 auto',
    zIndex: 10,
  },
  actBack: {
    flex: '0 0 auto',
    padding: '14px 16px',
    background: '#1A1814',
    color: '#9C9489',
    border: '1px solid #2A2620',
    borderRadius: '6px',
    fontSize: '11px',
    fontWeight: 700,
    letterSpacing: '0.15em',
    fontFamily: 'JetBrains Mono, monospace',
  },
  actReveal: {
    flex: 1,
    padding: '14px 20px',
    background: '#D4A24C',
    color: '#0F0E0C',
    borderRadius: '6px',
    fontSize: '12px',
    fontWeight: 800,
    letterSpacing: '0.2em',
    fontFamily: 'JetBrains Mono, monospace',
  },
  actSkip: {
    flex: '0 0 auto',
    padding: '14px 16px',
    background: '#1A1814',
    color: '#9C9489',
    border: '1px solid #2A2620',
    borderRadius: '6px',
    fontSize: '11px',
    fontWeight: 700,
    letterSpacing: '0.15em',
    fontFamily: 'JetBrains Mono, monospace',
  },
  actDrill: {
    flex: 1,
    padding: '14px 12px',
    background: 'transparent',
    color: '#E0A93C',
    border: '1px solid #5A4828',
    borderRadius: '6px',
    fontSize: '11px',
    fontWeight: 700,
    letterSpacing: '0.18em',
    fontFamily: 'JetBrains Mono, monospace',
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
    alignItems: 'center',
  },
  actMaster: {
    flex: 1,
    padding: '14px 12px',
    background: '#6FCF97',
    color: '#0F0E0C',
    borderRadius: '6px',
    fontSize: '11px',
    fontWeight: 800,
    letterSpacing: '0.18em',
    fontFamily: 'JetBrains Mono, monospace',
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
    alignItems: 'center',
  },
  actSkipSm: {
    flex: 1,
    padding: '14px 12px',
    background: 'transparent',
    color: '#6B645A',
    border: '1px solid #2A2620',
    borderRadius: '6px',
    fontSize: '11px',
    fontWeight: 700,
    letterSpacing: '0.18em',
    fontFamily: 'JetBrains Mono, monospace',
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
    alignItems: 'center',
  },
  actNum: {
    fontSize: '8px',
    opacity: 0.5,
    letterSpacing: '0.1em',
  },

  // stats panel
  overlay: {
    position: 'fixed',
    inset: 0,
    background: 'rgba(0,0,0,0.5)',
    backdropFilter: 'blur(4px)',
    zIndex: 50,
  },
  statsPanel: {
    position: 'fixed',
    top: 0,
    right: 0,
    bottom: 0,
    width: 'min(420px, 100vw)',
    background: '#0F0E0C',
    borderLeft: '1px solid #2A2620',
    padding: '24px',
    overflowY: 'auto',
    zIndex: 51,
    display: 'flex',
    flexDirection: 'column',
    gap: '24px',
  },
  statsHeader: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
  },
  statsTitle: {
    fontFamily: 'Fraunces, serif',
    fontSize: '20px',
    fontWeight: 600,
    letterSpacing: '0.1em',
    color: '#D4A24C',
  },
  statsSubtitle: {
    fontFamily: 'JetBrains Mono, monospace',
    fontSize: '10px',
    letterSpacing: '0.2em',
    color: '#6B645A',
    marginTop: '4px',
  },
  closeBtn: {
    background: 'transparent',
    color: '#9C9489',
    fontSize: '20px',
    padding: '4px 12px',
  },
  statsBigPct: {
    background: '#1A1814',
    border: '1px solid #2A2620',
    borderRadius: '4px',
    padding: '32px 20px',
    textAlign: 'center',
  },
  statsBigNum: {
    fontFamily: 'Fraunces, serif',
    fontSize: '64px',
    fontWeight: 600,
    color: '#D4A24C',
    lineHeight: 1,
    letterSpacing: '-0.02em',
  },
  statsPctSym: {
    fontSize: '32px',
    color: '#6B645A',
  },
  statsBigLabel: {
    fontFamily: 'JetBrains Mono, monospace',
    fontSize: '10px',
    color: '#9C9489',
    letterSpacing: '0.2em',
    marginTop: '12px',
  },
  catList: {
    display: 'flex',
    flexDirection: 'column',
    gap: '14px',
  },
  catRow: {
    display: 'flex',
    flexDirection: 'column',
    gap: '6px',
  },
  catRowTop: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'baseline',
  },
  catName: {
    fontFamily: 'Manrope, sans-serif',
    fontSize: '13px',
    fontWeight: 600,
    color: '#F0EBE0',
    letterSpacing: '0.02em',
  },
  catCount: {
    fontFamily: 'JetBrains Mono, monospace',
    fontSize: '11px',
    color: '#9C9489',
  },
  catBar: {
    height: '3px',
    background: '#1A1814',
    borderRadius: '2px',
    overflow: 'hidden',
  },
  catBarFill: {
    height: '100%',
    background: '#D4A24C',
    transition: 'width 0.4s ease',
  },
  resetBtn: {
    marginTop: 'auto',
    padding: '12px',
    background: 'transparent',
    color: '#6B645A',
    border: '1px solid #2A2620',
    borderRadius: '6px',
    fontSize: '10px',
    fontWeight: 700,
    letterSpacing: '0.2em',
    fontFamily: 'JetBrains Mono, monospace',
  },
};
