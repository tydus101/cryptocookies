using Prism.Commands;
using Prism.Mvvm;
using Prism.Navigation;
using SkiaSharp;
using SkiaSharp.Views.Forms;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Windows.Input;
using Xamarin.Forms;

namespace CookieCutter.ViewModels
{
    public class MainPageViewModel : ViewModelBase
    {
        private String _imgSrc;
        private Random r;
        private List<String> imageDB;
        public MainPageViewModel(INavigationService navigationService)
            : base(navigationService)
        {
            Title = "Cookie Cutter Generator";
            submitCommand = new Command(selectImage);
            r = new Random();
            imageDB = new List<String>
            {
                "example.png", "example1.png", "example2.png", "example3.png", "example4.png", "example5.png", "example6.png", "example7.png"
            };
          

        }

        


        public string imgSrc
        {
            get { return _imgSrc; }
            set
            {
                SetProperty(ref _imgSrc, value, "imgSrc");
            }
        }
        public void selectImage()
        {
            imgSrc = imageDB[r.Next(0, imageDB.Count)];
        }
        public ICommand submitCommand { private set; get; }

        public String IntroPancakeText
        {
            get
            {
                return "We randomly generated a seed, which \n creates random values from[0, 1]. Depending \non what text you type we construct a series of \n Bézier curves and form a path.Using Blender \n this path gets turned into a custom Cookie\nCutter just for you!";
            }
        }


        public class SkiaEventArgsConverter : IValueConverter
        {
            public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
            {
                var sKPaintSurfaceEventArgs = value as SKPaintSurfaceEventArgs;
                if (sKPaintSurfaceEventArgs == null)
                {
                    throw new ArgumentException("Expected value to be of type SKPaintSurfaceEventArgs", nameof(value));
                }

                return sKPaintSurfaceEventArgs;
            }

            public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
            {
                throw new NotImplementedException();
            }

          
        }

        SKPaint backgroundBrush = new SKPaint()
        {
            Style = SKPaintStyle.Fill,
            Color = Color.Red.ToSKColor()
        };

        private void BackgroundGradient_PaintSurface(object sender, SkiaSharp.Views.Forms.SKPaintSurfaceEventArgs e)
        {
            SKImageInfo info = e.Info;
            SKSurface surface = e.Surface;
            SKCanvas canvas = surface.Canvas;

            canvas.Clear();

            // get the brush based on the theme
            SKColor gradientStart = ((Color)Application.Current.Resources["BackgroundGradientStartColor"]).ToSKColor();
            SKColor gradientMid = ((Color)Application.Current.Resources["BackgroundGradientMidColor"]).ToSKColor();
            SKColor gradientEnd = ((Color)Application.Current.Resources["BackgroundGradientEndColor"]).ToSKColor();

            // gradient backround
            /*backgroundBrush.Shader = SKShader.CreateRadialGradient
                (new SKPoint(0, info.Height * .8f),
                info.Height * .8f,
                new SKColor[] { gradientStart, gradientMid, gradientEnd },
                new float[] { 0, .5f, 1 },
                SKShaderTileMode.Clamp);*/

            backgroundBrush.Shader = SKShader.CreateLinearGradient(
                                         new SKPoint(0, 0),
                                         new SKPoint(info.Width, info.Height),
                                         new SKColor[] {
                                             gradientStart, gradientEnd },
                                         new float[] { 0, 1 },
                                          SKShaderTileMode.Clamp);
            SKRect backgroundBounds = new SKRect(0, 0, info.Width, info.Height);
            canvas.DrawRect(backgroundBounds, backgroundBrush);


        }
    }
}
