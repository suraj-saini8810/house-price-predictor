import pickle
import warnings
warnings.filterwarnings('ignore')

print("🏠 HOUSE PRICE PREDICTION SYSTEM 🏠")
print("=====================================")
print("Please enter the following details about your house:")
print()

# Load the model
m1 = "module.pickle"
try:
    a = pickle.load(open(m1, "rb"))
    print("✅ AI Model loaded successfully!")
    print()
except:
    print("❌ Error: Model file not found. Please run the training script first.")
    exit()

# Get user inputs with explanations
print("📝 HOUSE DETAILS:")
print("-" * 40)

aa = int(input("🛏️  Number of bedrooms (e.g., 3): "))
print()

bb = int(input("🚿 Number of bathrooms (e.g., 2): "))
print()

print("🏠 Living area = The indoor space inside your house")
cc = int(input("   Enter living area in square feet (e.g., 1500): "))
print()

print("📐 Lot size = The total land your property sits on")
dd = int(input("   Enter lot size in square feet (e.g., 5000): "))
print()

ee = int(input("🏢 Number of floors (1, 2, or 3): "))
print()

print("🌊 Is your house on a waterfront?")
waterfront_input = input("   Enter Yes or No: ").lower()
if waterfront_input in ['yes', 'y']:
    ff = 1
elif waterfront_input in ['no', 'n']:
    ff = 0
else:
    print("   Invalid input, assuming No")
    ff = 0
print()

gg = int(input("⬆️  Above ground area in sq ft (e.g., 1200): "))
print()

hh = int(input("⬇️  Basement area in sq ft (e.g., 300, or 0 if no basement): "))
print()

ii = int(input("📅 Year the house was built (e.g., 1995): "))
print()

print("🔮 MAKING PREDICTION...")
print("=" * 40)

# Make prediction
try:
    s = a.predict([[aa, bb, cc, dd, ee, ff, gg, hh, ii]])
    
    # Display result - format as currency
    predicted_price = s[0]
    print(f"🎯 Predicted House Price: ${predicted_price:,.2f}")
    
    # Give price range context
    if predicted_price < 300000:
        price_category = "💚 Affordable Range"
    elif predicted_price < 600000:
        price_category = "💛 Mid-Range"
    elif predicted_price < 1000000:
        price_category = "🧡 High-End"
    else:
        price_category = "💎 Luxury"
    
    print(f"🏷️  Price Category: {price_category}")
    
    # Note: LinearRegression doesn't have confidence levels like classification
    print("📊 This prediction is based on similar houses in the dataset")
        
except Exception as e:
    print(f"❌ Error making prediction: {e}")

print()
print("✨ Thank you for using the House Price Predictor! ✨")