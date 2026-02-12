
from openpyxl import load_workbook
import sys

try:
    wb = load_workbook("output_showcase/market_sizing_中国无糖茶饮料市场_20260212.xlsx", data_only=False)
    
    print("=== Sheet 1: 核心假设 ===")
    ws1 = wb["核心假设"]
    print(f"B5 Value: {ws1['B5'].value} (Should be 9.3)")
    
    print("\n=== Sheet 2: Fermi Calculation ===")
    ws2 = wb["Fermi_Calc"]
    print(f"C4 Formula: {ws2['C4'].value}")
    print(f"C5 Formula: {ws2['C5'].value}")
    print(f"C8 Formula: {ws2['C8'].value}")
    
    print("\n=== Sheet 3: Market Size ===")
    ws3 = wb["Market_Size_Output"]
    print(f"B5 (SAM) Formula: {ws3['B5'].value}")
    print(f"B6 (SOM) Formula: {ws3['B6'].value}")
    
    print("\n=== Sheet 4: Growth Forecast ===")
    ws4 = wb["Growth_Forecast"]
    print(f"B5 (2025 TAM) Formula: {ws4['B5'].value}")
    
    print("\n✅ Verification Complete")
except Exception as e:
    print(f"❌ Error: {e}")
