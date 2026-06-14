"""Rule-based fitness coach for gym info, workout, and diet plans."""

GYM_INFO = {
    'hours': 'Open 24/7 | Staffed: 7am – 9pm daily',
    'location': 'Gota, Ahmedabad, Gujarat',
    'phone': '54127 54786',
    'email': 'gympro10@gmail.com',
    'plans': {
        'starter': {'name': 'Starter', 'price': '₹6,000/mo', 'features': ['24/7 access', '1 intro session', 'Locker & showers']},
        'pro': {'name': 'Pro', 'price': '₹10,000/mo', 'features': ['Everything in Starter', 'Weekly group classes', 'Monthly body scan']},
        'elite': {'name': 'Elite Coaching', 'price': '₹15,000/mo', 'features': ['1:1 coaching (4x/mo)', 'Nutrition roadmap', 'Recovery labs']},
    },
    'trainers': [
        'Tarun Kapoor – Strength & Hypertrophy',
        'Nitesh Soni – Conditioning & HIIT',
        'Soniya Patel – Mobility & Recovery',
        'Raj Kapoor – Nutrition Coaching',
    ],
}

WORKOUT_TEMPLATES = {
    'weight_loss': {
        'beginner': [
            {'day': 'Mon', 'focus': 'Full Body + Cardio', 'exercises': ['Treadmill 20 min', 'Goblet Squats 3×12', 'Push-ups 3×10', 'Rows 3×12', 'Plank 3×30s']},
            {'day': 'Wed', 'focus': 'HIIT Circuit', 'exercises': ['Jump rope 5 min', 'Burpees 3×8', 'Mountain climbers 3×20', 'Kettlebell swings 3×15', 'Bike 15 min']},
            {'day': 'Fri', 'focus': 'Strength + Walk', 'exercises': ['Leg press 3×12', 'Lat pulldown 3×12', 'Dumbbell press 3×10', 'Brisk walk 30 min']},
        ],
        'intermediate': [
            {'day': 'Mon', 'focus': 'Upper + Cardio', 'exercises': ['Bench press 4×10', 'Rows 4×10', 'Shoulder press 3×12', 'HIIT 15 min']},
            {'day': 'Tue', 'focus': 'Lower + Cardio', 'exercises': ['Squats 4×10', 'Romanian deadlift 3×10', 'Lunges 3×12', 'Stair climber 20 min']},
            {'day': 'Thu', 'focus': 'Full Body Circuit', 'exercises': ['Deadlifts 3×8', 'Pull-ups 3×8', 'Dips 3×10', 'Battle ropes 5×30s']},
            {'day': 'Sat', 'focus': 'Active Recovery', 'exercises': ['Yoga flow 30 min', 'Light jog 20 min', 'Stretching 15 min']},
        ],
        'advanced': [
            {'day': 'Mon', 'focus': 'Push + HIIT', 'exercises': ['Barbell bench 5×5', 'OHP 4×8', 'Tricep dips 4×12', 'Sprint intervals 10×30s']},
            {'day': 'Tue', 'focus': 'Pull + Cardio', 'exercises': ['Deadlift 5×5', 'Pull-ups 4×10', 'Barbell rows 4×8', 'Row machine 20 min']},
            {'day': 'Wed', 'focus': 'Legs', 'exercises': ['Back squats 5×5', 'Leg curl 4×12', 'Calf raises 4×15', 'Box jumps 4×8']},
            {'day': 'Fri', 'focus': 'Metcon', 'exercises': ['AMRAP 20 min: 10 KB swings, 10 push-ups, 200m run']},
            {'day': 'Sat', 'focus': 'Zone 2 Cardio', 'exercises': ['45 min steady-state cardio', 'Core circuit 15 min']},
        ],
    },
    'muscle_gain': {
        'beginner': [
            {'day': 'Mon', 'focus': 'Upper Body', 'exercises': ['Bench press 3×10', 'Lat pulldown 3×10', 'Shoulder press 3×10', 'Bicep curls 3×12']},
            {'day': 'Wed', 'focus': 'Lower Body', 'exercises': ['Squats 3×10', 'Leg press 3×12', 'Leg curl 3×12', 'Calf raises 3×15']},
            {'day': 'Fri', 'focus': 'Full Body', 'exercises': ['Deadlift 3×8', 'Incline press 3×10', 'Rows 3×10', 'Lateral raises 3×12']},
        ],
        'intermediate': [
            {'day': 'Mon', 'focus': 'Chest & Triceps', 'exercises': ['Bench 4×8', 'Incline DB press 3×10', 'Cable flyes 3×12', 'Tricep pushdown 4×12']},
            {'day': 'Tue', 'focus': 'Back & Biceps', 'exercises': ['Barbell rows 4×8', 'Pull-ups 4×8', 'Face pulls 3×15', 'Hammer curls 3×12']},
            {'day': 'Thu', 'focus': 'Legs', 'exercises': ['Squats 4×8', 'Romanian DL 4×10', 'Leg press 3×12', 'Leg extensions 3×15']},
            {'day': 'Sat', 'focus': 'Shoulders & Arms', 'exercises': ['OHP 4×8', 'Lateral raises 4×12', 'Shrugs 3×12', 'Superset curls + dips']},
        ],
        'advanced': [
            {'day': 'Mon', 'focus': 'Push', 'exercises': ['Bench 5×5', 'OHP 4×6', 'Incline press 4×8', 'Skull crushers 4×10']},
            {'day': 'Tue', 'focus': 'Pull', 'exercises': ['Deadlift 5×3', 'Weighted pull-ups 4×6', 'Barbell rows 4×8', 'Barbell curls 4×10']},
            {'day': 'Wed', 'focus': 'Legs', 'exercises': ['Squats 5×5', 'Front squats 4×8', 'Leg press 4×10', 'Nordic curls 3×8']},
            {'day': 'Fri', 'focus': 'Upper Hypertrophy', 'exercises': ['DB press 4×12', 'Cable rows 4×12', 'Arnold press 3×12', 'Finisher: 100 push-ups']},
            {'day': 'Sat', 'focus': 'Lower Hypertrophy', 'exercises': ['Hack squats 4×10', 'Stiff-leg DL 4×10', 'Walking lunges 3×12', 'Calf raises 5×15']},
        ],
    },
    'general_fitness': {
        'beginner': [
            {'day': 'Mon', 'focus': 'Foundation', 'exercises': ['Bodyweight squats 3×12', 'Wall push-ups 3×12', 'Band rows 3×12', 'Walking 20 min']},
            {'day': 'Wed', 'focus': 'Mobility + Core', 'exercises': ['Cat-cow stretches', 'Bird dogs 3×10', 'Glute bridges 3×15', 'Light cycling 15 min']},
            {'day': 'Fri', 'focus': 'Full Body', 'exercises': ['Goblet squats 3×10', 'Dumbbell press 3×10', 'Lat pulldown 3×10', 'Plank 3×30s']},
        ],
        'intermediate': [
            {'day': 'Mon', 'focus': 'Strength', 'exercises': ['Squats 4×8', 'Bench 4×8', 'Rows 4×8', 'Core circuit 15 min']},
            {'day': 'Wed', 'focus': 'Conditioning', 'exercises': ['Circuit: 5 rounds of 10 KB swings, 10 box step-ups, 30s rest']},
            {'day': 'Fri', 'focus': 'Functional', 'exercises': ['Deadlifts 4×6', 'Pull-ups 4×6', 'Farmer carries 4×40m', 'Stretch 15 min']},
        ],
        'advanced': [
            {'day': 'Mon', 'focus': 'Power', 'exercises': ['Power cleans 5×3', 'Front squats 4×5', 'Box jumps 4×5']},
            {'day': 'Wed', 'focus': 'Athletic', 'exercises': ['Sprints 8×40m', 'Medicine ball slams 4×10', 'Turkish get-ups 3×5/side']},
            {'day': 'Fri', 'focus': 'Strength Endurance', 'exercises': ['EMOM 20 min: 5 pull-ups, 10 push-ups, 15 squats']},
        ],
    },
    'endurance': {
        'beginner': [
            {'day': 'Mon', 'focus': 'Cardio Base', 'exercises': ['Brisk walk/jog 25 min', 'Bodyweight circuit 2 rounds']},
            {'day': 'Wed', 'focus': 'Cycling', 'exercises': ['Stationary bike 30 min steady', 'Core: planks & dead bugs']},
            {'day': 'Fri', 'focus': 'Mixed', 'exercises': ['Row machine 20 min', 'Light resistance band work']},
        ],
        'intermediate': [
            {'day': 'Mon', 'focus': 'Tempo Run', 'exercises': ['Warm-up 10 min', 'Tempo 20 min', 'Cool-down 10 min']},
            {'day': 'Wed', 'focus': 'Cross Training', 'exercises': ['Swim or bike 40 min', 'Strength maintenance 20 min']},
            {'day': 'Fri', 'focus': 'Intervals', 'exercises': ['6×3 min hard / 2 min easy', 'Mobility 15 min']},
        ],
        'advanced': [
            {'day': 'Mon', 'focus': 'Long Run', 'exercises': ['60 min zone 2 run', 'Hip mobility']},
            {'day': 'Wed', 'focus': 'Threshold', 'exercises': ['Warm-up', '3×10 min at threshold', 'Cool-down']},
            {'day': 'Fri', 'focus': 'Speed + Strength', 'exercises': ['Hill sprints 10×30s', 'Single-leg strength 30 min']},
        ],
    },
}

DIET_TEMPLATES = {
    'weight_loss': {
        'calories_note': 'Aim for ~300–500 cal deficit from maintenance.',
        'meals': {
            'breakfast': ['Oats with berries & almonds', '2 boiled eggs', 'Green tea'],
            'lunch': ['Grilled chicken salad', 'Brown rice (small portion)', 'Mixed vegetables'],
            'snack': ['Greek yogurt', 'Handful of nuts'],
            'dinner': ['Baked fish or paneer', 'Steamed veggies', 'Small portion quinoa'],
        },
        'tips': ['Drink 3L water daily', 'Limit sugar & fried food', 'Eat protein at every meal'],
    },
    'muscle_gain': {
        'calories_note': 'Aim for ~300–500 cal surplus with high protein.',
        'meals': {
            'breakfast': ['4 egg omelette with veggies', 'Whole grain toast', 'Banana smoothie with protein'],
            'lunch': ['Chicken/paneer curry', 'Brown rice', 'Dal + salad'],
            'snack': ['Protein shake', 'Peanut butter sandwich'],
            'dinner': ['Grilled steak/soya chunks', 'Sweet potato', 'Broccoli'],
        },
        'tips': ['1.6–2g protein per kg bodyweight', 'Eat every 3–4 hours', 'Post-workout protein within 30 min'],
    },
    'general_fitness': {
        'calories_note': 'Balanced calories at maintenance level.',
        'meals': {
            'breakfast': ['Poha or upma with vegetables', 'Fruit', 'Milk or lassi'],
            'lunch': ['Roti (2)', 'Dal', 'Sabzi', 'Curd'],
            'snack': ['Fruit + handful of nuts'],
            'dinner': ['Grilled protein', 'Salad', 'Soup'],
        },
        'tips': ['Balanced macros: 40% carbs, 30% protein, 30% fats', 'Stay hydrated', 'Minimize processed food'],
    },
    'endurance': {
        'calories_note': 'Moderate surplus on training days; carbs fuel performance.',
        'meals': {
            'breakfast': ['Oats with honey & banana', 'Toast with peanut butter'],
            'lunch': ['Pasta or rice bowl', 'Lean protein', 'Vegetables'],
            'snack': ['Energy bar or dates', 'Electrolyte drink'],
            'dinner': ['Fish/chicken', 'Complex carbs', 'Leafy greens'],
        },
        'tips': ['Carb-load before long sessions', 'Replenish within 45 min post-workout', 'Include iron-rich foods'],
    },
}


def get_gym_info(topic=None):
    if not topic or topic == 'general':
        return (
            f"**GYM PRO** – Train Different!\n\n"
            f"📍 {GYM_INFO['location']}\n"
            f"🕐 {GYM_INFO['hours']}\n"
            f"📞 {GYM_INFO['phone']}\n"
            f"✉️ {GYM_INFO['email']}\n\n"
            f"**Membership Plans:**\n"
            + '\n'.join(
                f"• **{p['name']}** – {p['price']}: {', '.join(p['features'])}"
                for p in GYM_INFO['plans'].values()
            )
            + f"\n\n**Our Trainers:**\n"
            + '\n'.join(f"• {t}" for t in GYM_INFO['trainers'])
        )
    if topic == 'plans':
        return '\n'.join(
            f"**{p['name']}** – {p['price']}\n  " + '\n  '.join(f"✓ {f}" for f in p['features'])
            for p in GYM_INFO['plans'].values()
        )
    if topic == 'trainers':
        return "**Meet Our Trainers:**\n" + '\n'.join(f"• {t}" for t in GYM_INFO['trainers'])
    if topic == 'contact':
        return f"📍 {GYM_INFO['location']}\n📞 {GYM_INFO['phone']}\n✉️ {GYM_INFO['email']}\n🕐 {GYM_INFO['hours']}"
    return get_gym_info('general')


def generate_workout_plan(goal, level, days_per_week=3):
    goal = goal if goal in WORKOUT_TEMPLATES else 'general_fitness'
    level = level if level in ('beginner', 'intermediate', 'advanced') else 'beginner'
    sessions = WORKOUT_TEMPLATES[goal][level][:min(int(days_per_week), 5)]

    goal_labels = {
        'weight_loss': 'Fat Loss',
        'muscle_gain': 'Muscle Building',
        'general_fitness': 'General Fitness',
        'endurance': 'Endurance',
    }
    lines = [
        f"**Your {goal_labels.get(goal, goal)} Workout Plan** ({level.title()}, {len(sessions)} days/week)\n"
    ]
    for s in sessions:
        lines.append(f"\n**{s['day']} – {s['focus']}**")
        for ex in s['exercises']:
            lines.append(f"  • {ex}")
    lines.append("\n💡 Warm up 5–10 min before each session. Rest 48h between same muscle groups.")
    return '\n'.join(lines)


def generate_diet_plan(goal, weight_kg=None):
    goal = goal if goal in DIET_TEMPLATES else 'general_fitness'
    diet = DIET_TEMPLATES[goal]
    goal_labels = {
        'weight_loss': 'Fat Loss',
        'muscle_gain': 'Muscle Gain',
        'general_fitness': 'Balanced Fitness',
        'endurance': 'Endurance Athlete',
    }
    lines = [f"**{goal_labels.get(goal, goal)} Diet Plan**\n", diet['calories_note']]
    if weight_kg:
        try:
            w = float(weight_kg)
            protein = round(w * 1.8) if goal == 'muscle_gain' else round(w * 1.4)
            lines.append(f"Suggested daily protein: ~{protein}g (based on {w}kg bodyweight)")
        except (TypeError, ValueError):
            pass
    for meal, items in diet['meals'].items():
        lines.append(f"\n**{meal.title()}**")
        for item in items:
            lines.append(f"  • {item}")
    lines.append("\n**Tips:**")
    for tip in diet['tips']:
        lines.append(f"  ✓ {tip}")
    return '\n'.join(lines)


def process_message(message, context=None):
    """Process a user message and return a response with optional updated context."""
    context = context or {}
    msg = message.lower().strip()

    if msg in ('gym info', 'info', 'about gym', 'membership', 'plans', 'trainers', 'contact', 'hours'):
        topic_map = {
            'membership': 'plans', 'plans': 'plans', 'trainers': 'trainers',
            'contact': 'contact', 'hours': 'contact',
        }
        return {'reply': get_gym_info(topic_map.get(msg, 'general')), 'context': {}}

    if msg in ('workout', 'workout plan', 'gym plan', 'training plan', 'exercise'):
        return {
            'reply': "Let's build your workout plan! What's your **fitness goal**?\n\nChoose: **weight loss**, **muscle gain**, **general fitness**, or **endurance**",
            'context': {'step': 'workout_goal'},
        }

    if msg in ('diet', 'diet plan', 'nutrition', 'meal plan', 'food'):
        return {
            'reply': "Let's create your diet plan! What's your **fitness goal**?\n\nChoose: **weight loss**, **muscle gain**, **general fitness**, or **endurance**",
            'context': {'step': 'diet_goal'},
        }

    step = context.get('step')

    if step == 'workout_goal' and msg in WORKOUT_TEMPLATES:
        return {
            'reply': f"Great choice! What's your **experience level**?\n\nChoose: **beginner**, **intermediate**, or **advanced**",
            'context': {'step': 'workout_level', 'goal': msg},
        }

    if step == 'workout_level' and msg in ('beginner', 'intermediate', 'advanced'):
        return {
            'reply': "How many days per week can you train? (Enter **3**, **4**, or **5**)",
            'context': {'step': 'workout_days', 'goal': context.get('goal'), 'level': msg},
        }

    if step == 'workout_days':
        days = 3
        for d in ('5', '4', '3'):
            if d in msg:
                days = int(d)
                break
        plan = generate_workout_plan(context.get('goal'), context.get('level'), days)
        return {
            'reply': plan + "\n\nWant a **diet plan** too? Just type **diet plan**!",
            'context': {},
        }

    if step == 'diet_goal' and msg in DIET_TEMPLATES:
        return {
            'reply': "What's your **body weight in kg**? (e.g. 70) — or type **skip** for a general plan.",
            'context': {'step': 'diet_weight', 'goal': msg},
        }

    if step == 'diet_weight':
        weight = None
        if msg != 'skip':
            try:
                weight = float(''.join(c for c in msg if c.isdigit() or c == '.'))
            except ValueError:
                pass
        plan = generate_diet_plan(context.get('goal'), weight)
        return {
            'reply': plan + "\n\nNeed a **workout plan**? Type **workout plan**!",
            'context': {},
        }

    if any(w in msg for w in ('hello', 'hi', 'hey', 'help')):
        return {
            'reply': (
                "Hey! I'm **FitBot**, your GYM PRO fitness assistant. I can help with:\n\n"
                "• **Gym info** – hours, plans, trainers\n"
                "• **Workout plan** – personalized training schedule\n"
                "• **Diet plan** – nutrition based on your goals\n\n"
                "Tap a quick button below or type your question!"
            ),
            'context': {},
        }

    return {
        'reply': (
            "I'm not sure about that, but I can help with **gym info**, **workout plans**, or **diet plans**. "
            "Try one of the quick options below!"
        ),
        'context': context,
    }
