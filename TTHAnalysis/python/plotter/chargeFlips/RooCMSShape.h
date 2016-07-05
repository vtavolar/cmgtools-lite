/*****************************************************************************
 * Project: CMS detector at the CERN
 *
 * Package: PhysicsTools/TagAndProbe/RooCMSShape
 *
 *
 * Authors:
 *   Nadia Adam, Princeton - neadam@princeton.edu
 *   Adam Hunt, Princeton  - ahunt@princeton.edu
 *   Kalanand Mishra, Fermilab - kalanand@fnal.gov
 *
 * Description:
 *   Defines a probability density function which has exponential decay
 *   distribution at high mass beyond the pole position (say, Z peak)
 *   but turns over (i.e., error function) at low mass due to threshold
 *   effect. We use this to model the background shape in Z->ll invariant
 *   mass.
 * History:
 *
 * *****************************
 * Copied from: https://cmssdt.cern.ch/SDT/doxygen/CMSSW_8_0_6/doc/html/dc/d02/RooCMSShape_8h.html
 * *****************************
 *
 *****************************************************************************/

#ifndef ROO_CMS_SHAPE
#define ROO_CMS_SHAPE

#include "RooAbsPdf.h"
#include "RooRealProxy.h"
#include "RooAbsReal.h"
#include "TMath.h"
#include "RooMath.h"

class RooCMSShape : public RooAbsPdf {
public:
  RooCMSShape() {};
  RooCMSShape(const char *name, const char *title,
          RooAbsReal& _x,
          RooAbsReal& _alpha,
          RooAbsReal& _beta,
          RooAbsReal& _gamma,
          RooAbsReal& _peak);

  RooCMSShape(const RooCMSShape& other, const char* name);
  inline virtual TObject* clone(const char* newname) const { return new RooCMSShape(*this,newname); }
  inline ~RooCMSShape() {}
  Double_t evaluate() const ;

protected:

  RooRealProxy x ;
  RooRealProxy alpha ;
  RooRealProxy beta ;
  RooRealProxy gamma ;
  RooRealProxy peak ;

};

RooCMSShape::RooCMSShape(const char *name, const char *title,
                       RooAbsReal& _x,
                       RooAbsReal& _alpha,
                       RooAbsReal& _beta,
                       RooAbsReal& _gamma,
                       RooAbsReal& _peak) :
  RooAbsPdf(name,title),
  x("x","x",this,_x),
  alpha("alpha","alpha",this,_alpha),
  beta("beta","beta",this,_beta),
  gamma("gamma","gamma",this,_gamma),
  peak("peak","peak",this,_peak)
{ }
RooCMSShape::RooCMSShape(const RooCMSShape& other, const char* name):
  RooAbsPdf(other,name),
  x("x",this,other.x),
  alpha("alpha",this,other.alpha),
  beta("beta",this,other.beta),
  gamma("gamma",this,other.gamma),
  peak("peak",this,other.peak)
{ }
Double_t RooCMSShape::evaluate() const
{
 // ENTER EXPRESSION IN TERMS OF VARIABLE ARGUMENTS HERE
 //Double_t erf = TMath::Erfc((alpha - x) * beta);
 Double_t erf = RooMath::erfc((alpha - x) * beta);
 Double_t u = (x - peak)*gamma;
 if(u < -70) u = 1e20;
 else if( u>70 ) u = 0;
 else u = exp(-u);   //exponential decay
 return erf*u;
}

#endif

