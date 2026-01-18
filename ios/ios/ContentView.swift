//
//  ContentView.swift
//  ios
//
//  Created by Ethan Parker Wong on 2026-01-17.
//

import SwiftUI

struct ContentView: View {
    @State private var showHomeView: Bool = false
    @State private var textOpacity: Double = 0
    var body: some View {
     
        ZStack(alignment: .bottom){
                // this rectangle receives tap to trigger change to next screen
               
                if !showHomeView{
                    // move bg view out of this if we want music/vid to continue in ap duration 
                    BackgroundView(videoName: "VideoStar", videoType: "mov")
                        .ignoresSafeArea()
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                        .allowsHitTesting(false)
                    
                    
                    Text("tap to start")
                        .opacity(textOpacity)
                        .padding(.bottom, 30)
                        .font(.system(size: 30, design: .rounded))
                        .foregroundColor(.white)
                        .onAppear() {
                            withAnimation(.easeIn(duration: 1.5)) {
                                textOpacity = 1
                            }
                        }
                        
                    
                    
                    
                    Rectangle()
                        .fill(Color.clear)
                        .contentShape(Rectangle()) // needed to make the content a tappable area
                        .onTapGesture {
                            withAnimation(.linear(duration: 0.5)) {
                                showHomeView = true
                            }
                        }
                    
                }
                if showHomeView {
                    HomeView()
                        .transition(.opacity)
                        .ignoresSafeArea()
                        .frame(maxWidth: .infinity, maxHeight: .infinity)
                }
            }
        }
            
                
        
      
    
}

#Preview {
    ContentView()
}
