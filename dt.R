#Menambahkan library
library(C50)

#Mempersiapkan data
data <- read.csv("C:/Data/Work/Garda Adhikarya IPB'53/Chronous Ilkom 53/Tugas/Kecerdasan Buatan/projek/hasil/dataset_final.csv", header=TRUE)
summary(data)
set.seed(5674)

#Mengubah tipe data
data$CHARSET <- as.factor(data$CHARSET)
data$SERVER <- as.factor(data$SERVER)
data$WHOIS_COUNTRY <- as.factor(data$WHOIS_COUNTRY)
data$WHOIS_STATEPRO <- as.factor(data$WHOIS_STATEPRO)
data$WHOIS_REGDATE <- as.factor(data$WHOIS_REGDATE)
data$WHOIS_UPDATED_DATE <- as.factor(data$WHOIS_UPDATED_DATE)
data$Type <- as.factor(data$Type)
summary(data)

#Membagi data per kelas
vars <- c("URL_LENGTH", "NUMBER_SPECIAL_CHARACTERS", "CHARSET", "SERVER", "CONTENT_LENGTH", "WHOIS_COUNTRY", 
          "WHOIS_STATEPRO", "TCP_CONVERSATION_EXCHANGE", "DIST_REMOTE_TCP_PORT", "REMOTE_IPS", "APP_BYTES",
          "SOURCE_APP_PACKETS", "REMOTE_APP_PACKETS", "SOURCE_APP_BYTES", "REMOTE_APP_BYTES", "APP_PACKETS",
          "DNS_QUERY_TIMES")
str(data[, c(vars, "Type")])
data <- data[sample(nrow(data)),]
dataClass0 <- data[which(data$Type == '0'),]
dataClass0 <- data[sample(nrow(dataClass0)),]
dataClass1 <- data[which(data$Type == '1'),]
dataClass1 <- data[sample(nrow(dataClass1)),]

#10 folds
##Membuat 10 folds
foldsClass0 <- cut(seq(1,nrow(dataClass0)), breaks = 10, labels = FALSE)
foldsClass1 <- cut(seq(1,nrow(dataClass1)), breaks = 10, labels = FALSE)

sumAccuracy = 0
for(i in 1:10){
  ##Membagi ke dalam folds ke-i
  indexClass0 <- which(foldsClass0 == i, arr.ind = TRUE)
  indexClass1 <- which(foldsClass1 == i, arr.ind = TRUE)
  testDataClass0 <- dataClass0[indexClass0,]
  trainDataClass0 <- dataClass0[-indexClass0,]
  testDataClass1 <- dataClass1[indexClass1,]
  trainDataClass1 <- dataClass1[-indexClass1,]
  testData <- rbind(testDataClass1,testDataClass0)
  trainData <- rbind(trainDataClass1,trainDataClass0)
  assign(paste0("dataTest",i), testData)
  assign(paste0("dataTrain",i), trainData)
  
  ##Membuat model pohon keputusan
  treeModel <- C5.0.default(x = trainData[,vars], y = trainData$Type)
  assign(paste0("treeModel",i), treeModel)
  
  ##Menghitung akurasi
  predict <- (predict(treeModel, testData))
  sum=0
  for (j in 1:nrow(testData)){
    if(predict[j] == testData$Type[j])
      sum = sum + 1
  }
  accuracy <- sum/nrow(testData)*100
  assign(paste0("accuracyFold",i), accuracy)
  sumAccuracy = sumAccuracy + accuracy
}

#Menghitung rata-rata akurasi
avgAccuracy = sumAccuracy/10