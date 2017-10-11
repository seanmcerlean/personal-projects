namespace CalculatorTest.PageObjects
{
    using System.Collections.Generic;
    using System.Windows.Automation;

    class KeypadUI
    {
        private AutomationElement CalculatorWindow;
        private Dictionary<string, string> UIMap = new Dictionary<string, string>()
        {
            ["0"] = "130",
            ["1"] = "131",
            ["2"] = "132",
            ["3"] = "133",
            ["4"] = "134",
            ["5"] = "135",
            ["6"] = "136",
            ["7"] = "137",
            ["8"] = "138",
            ["9"] = "139",
            ["+"] = "93",
            ["-"] = "94",
            ["="] = "121",
            ["C"] = "81",
            ["CE"] = "82",
            ["ResultArea"] = "150"
        };

        public KeypadUI(int processId)
        {
            var processWithId = new PropertyCondition(AutomationElement.ProcessIdProperty, processId);
            CalculatorWindow = AutomationElement.RootElement.FindFirst(TreeScope.Children, processWithId);
        }

        public void Press(string key)
        {
            if (UIMap.ContainsKey(key))
            {
                var keyIdCondition = new PropertyCondition(AutomationElement.AutomationIdProperty, UIMap[key]);
                var buttonElement = CalculatorWindow.FindFirst(TreeScope.Descendants, keyIdCondition);
                var canInvoke = buttonElement.TryGetCurrentPattern(InvokePattern.Pattern, out object patternObject);

                if (canInvoke)
                {
                    var invokePattern = patternObject as InvokePattern;
                    invokePattern.Invoke();
                }
                else
                {
                    throw new ElementNotEnabledException("Button cannot be invoked");
                }
            }
            else
            {
                throw new ElementNotAvailableException("Unknown button");
            }
        }

        public void EnterDigits(string digits)
        {
            foreach (var digit in digits)
            {
                Press(digit.ToString());
            }
        }

        public string GetResult()
        {
            var resultIdCondition = new PropertyCondition(AutomationElement.AutomationIdProperty, UIMap["ResultArea"]);
            var resultAreaElement = CalculatorWindow.FindFirst(TreeScope.Descendants, resultIdCondition);
            // Name property reflects value shown on screen
            return resultAreaElement.Current.Name;
        }
    }
}
