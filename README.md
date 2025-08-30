# 🏠 House Price Predictor

A simple machine learning project that predicts house prices based on various features like bedrooms, bathrooms, living area, and more.

## 🎯 Features

- **User-friendly interface** with clear input prompts
- **Real-time price prediction** using trained ML models
- **Price categorization** (Affordable, Mid-range, High-end, Luxury)
- **Easy-to-understand results** with emoji indicators

## 🛠️ Technologies Used

- **Python 3.13**
- **scikit-learn** - Machine learning algorithms
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **pickle** - Model serialization

## 📋 Requirements

```bash
pip install pandas numpy scikit-learn
```

## 🚀 How to Use

### 1. Train the Model
```bash
python train.py
```
This will:
- Load the housing dataset
- Train the machine learning model
- Save the trained model as `module.pickle`

### 2. Make Predictions
```bash
python predict.py
```
This will:
- Load the trained model
- Ask for house details (bedrooms, bathrooms, etc.)
- Predict the house price
- Show the price category

## 📊 Sample Input/Output

```
🏠 HOUSE PRICE PREDICTION SYSTEM 🏠
Please enter the following details about your house:

🛏️  Number of bedrooms (e.g., 3): 4
🚿 Number of bathrooms (e.g., 2): 3
🏠 Living area in square feet (e.g., 1500): 2500
...

🎯 Predicted House Price: $1,197,933.63
🏷️ Price Category: 💎 Luxury
```

## 📁 Project Structure

```
├── train.py              # Model training script
├── predict.py            # Price prediction script  
├── kc_house_data.csv     # Housing dataset
├── module.pickle         # Trained model (generated)
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## 🔮 How It Works

1. **Training**: Uses Linear Regression to learn from historical house data
2. **Features**: Analyzes 9 key house characteristics
3. **Prediction**: Estimates price based on similar houses in the dataset

## 🎨 Features Explained

- **Living Area**: Indoor space (kitchen, bedrooms, living room)
- **Lot Size**: Total land area your property sits on
- **Waterfront**: Whether house has water view (beach, lake, river)
- **Above Ground**: Main floor area (excluding basement)
- **Basement**: Underground/below-grade area

## 📈 Future Improvements

- [ ] Add more advanced ML algorithms
- [ ] Include data visualization
- [ ] Add model accuracy metrics
- [ ] Web interface using Flask/Streamlit
- [ ] Real estate API integration

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---
**Made with ❤️ by [Your Name]**
